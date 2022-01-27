import isbnlib
import datetime
from typing import List

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

    def __init__(self, doc_id, get_meta_from_file=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.doc_id = doc_id
        self.get_meta_from_file = get_meta_from_file

    def run(self):
        doc: Document = get_session().get(Document, self.doc_id)
        if self.get_meta_from_file:
            meta = extract_meta(doc.path)
        else:
            meta = {'isbn': doc.isbn, 'doi': doc.doi}
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

    @staticmethod
    def _process_author(doc: Document, author: List[str], session):

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
        author, created = get_or_create(Author,
                                        first_name=first_name,
                                        last_name=last_name,
                                        middle_name=middle_name)
        if created:
            author.documents.append(doc)
            session.add(author)
            session.commit()
        mutex.unlock()

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
                    cls._process_author(doc, author, session)
                doc.title = isbn_meta.get('Title', None)
                doc.publication = isbn_meta.get('Publisher', None)
                doc.date = datetime.date(year=int(isbn_meta['Year']), day=1, month=1) if 'Year' in isbn_meta else None
                doc.language = isbn_meta.get('Language', None)

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
                doc.title = doi_meta['title'][0]
                doc.doi = doi_meta['DOI']
                doc.issue = doi_meta.get('issue', None)
                doc.volume = doi_meta.get('volume', None)
                for author in doi_meta.get('author', []):
                    author = [author['given'], author['family']]
                    cls._process_author(doc, author, session)
                # TODO: handle this meta properly in a separate function, this is ok for now
        except Exception as ex:
            logger.error(f'Could not update DOI metadata for {doc.path}: {ex}')

        mutex.lock()
        session.add(doc)
        session.commit()
        mutex.unlock()

