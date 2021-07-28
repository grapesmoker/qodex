import isbnlib
import datetime

from PySide6.QtCore import QObject, QThread, QMutex, Signal
from crossref_commons.retrieval import get_publication_as_json
from logging import getLogger
from qodex.db.models import Document, Author
from qodex.db.utils import get_or_create
from qodex.db.settings import get_session
from qodex.doctools.pdf import extract_meta


logger = getLogger(__name__)


mutex = QMutex()


class MetaUpdater(QThread):

    ready = Signal()

    def __init__(self, doc_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.doc_id = doc_id

    def run(self):
        doc = get_session().get(Document, self.doc_id)
        meta = extract_meta(doc.path)
        self.update_doc_meta(doc, meta)
        self.ready.emit()

    @staticmethod
    def fetch_meta(meta):

        try:
            if meta['isbn']:
                isbn_meta = isbnlib.meta(meta['isbn'])
            else:
                isbn_meta = {}
        except Exception as ex:
            logger.warning(f'Could not fetch ISBN data: {ex}')
            isbn_meta = {}

        print(isbn_meta)

        try:
            if meta['doi']:
                doi_meta = get_publication_as_json(meta['doi'])
            else:
                doi_meta = {}
        except Exception as ex:
            logger.warning(f'Could not fetch DOI data: {ex}')
            doi_meta = {}

        print(doi_meta)

        return isbn_meta, doi_meta

    @classmethod
    def update_doc_meta(cls, doc: Document, meta: dict):

        print('fetching meta')
        isbn_meta, doi_meta = cls.fetch_meta(meta)
        print('creating session')
        session = get_session()

        print('doing stuff')

        try:
            if isbn_meta:
                doc.isbn = isbn_meta.get('ISBN-13', None)
                for author in isbn_meta.get('Authors', []):
                    author = author.split()
                    if len(author) == 1:
                        first_name = author[0]
                        last_name = None
                    else:
                        first_name, last_name = author[0], author[-1]
                    if len(author) > 2:
                        middle_name = ' '.join(author[1:-1])
                    else:
                        middle_name = None
                    mutex.lock()
                    author, _ = get_or_create(Author,
                                              first_name=first_name,
                                              last_name=last_name,
                                              middle_name=middle_name)
                    author.documents.append(doc)
                    session.add(author)
                    session.commit()
                    mutex.unlock()
                doc.title = isbn_meta.get('Title', None)
        except Exception as ex:
            logger.error(f'Could not update ISBN metadata for {doc.path}: {ex}')

        try:
            if doi_meta:
                print('doi')
                doc.doi = doi_meta.get('DOI', None)
                date_created = doi_meta.get('created', None)
                if date_created:
                    date_parts = date_created.get('date_parts', None)
                    if date_parts and isinstance(date_parts, list):
                        doc.date = datetime.date(**date_parts[0])
        except Exception as ex:
            logger.error(f'Could not update DOI metadata for {doc.path}: {ex}')

        mutex.lock()
        session.add(doc)
        session.commit()
        mutex.unlock()
