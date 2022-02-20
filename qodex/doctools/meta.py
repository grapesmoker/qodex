from PySide6.QtCore import QMutex
from logging import getLogger

logger = getLogger(__name__)


def unify_meta(isbn_meta, doi_meta):

    isbn_meta = isbn_meta or {}
    doi_meta = doi_meta or {}
    unified_meta = dict()

    unified_meta['isbn'] = isbn_meta.get('isbn-13', None) or isbn_meta.get('isbn-10', None)
    unified_meta['title'] = isbn_meta.get('title', None) or doi_meta.get('title', None)

    isbn_authors = isbn_meta.get('authors', None)
    doi_authors = doi_meta.get('author', None)

    if isbn_authors:
        unified_meta['authors'] = isbn_authors


