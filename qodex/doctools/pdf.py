import tika
import pyparsing as pp

from tika import parser
from pathlib import Path
from dataclasses import dataclass
from typing import List

tika.initVM()

isbn_parser = pp.Or([
    pp.Literal('ISBN-13'), pp.Literal('ISBN-10'), pp.Literal('ISBN 10'), pp.Literal('ISBN 13'),
    pp.Literal('ISBN')
]) + pp.Optional(':') + pp.Regex('([0-9]|-)+').setResultsName('isbn')

doi_parser = pp.Literal('DOI') + pp.Optional(':') + \
             pp.Regex('10\\.[0-9]{4,9}/[-._;()/:A-Za-z0-9]+').setResultsName('doi')


@dataclass
class DocumentMeta:

    isbn: str = None
    doi: str = None
    authors: List[str] = None
    title: str = None


def extract_meta(filename: Path) -> dict:
    doc = parser.from_file(str(filename))

    if not doc or 'content' not in doc or doc['content'] is None:
        return {'isbn': None, 'doi': None}

    isbn_index = doc['content'].find('ISBN')

    if isbn_index > 0:
        try:
            chunk = doc['content'][isbn_index:isbn_index + 100]
            isbn = isbn_parser.parseString(chunk)['isbn']
        except:
            isbn = None
    else:
        isbn = None

    doi_index = doc['content'].find('DOI')

    if doi_index > 0:
        try:
            chunk = doc['content'][doi_index:doi_index + 100]
            doi = doi_parser.parseString(chunk)['doi']
        except:
            doi = None
    else:
        doi = None

    return {'isbn': isbn, 'doi': doi}
