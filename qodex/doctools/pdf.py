import subprocess
from uuid import uuid4

import tika
import pyparsing as pp

from tika import parser
from pathlib import Path
from dataclasses import dataclass
from typing import List

tika.initVM()

isbn_parser = pp.Or([
    pp.Literal('ISBN-13'),
    pp.Literal('ISBN-10'),
    pp.Literal('ISBN 13'),
    pp.Literal('ISBN 10'),
    pp.Literal('ISBN13'),
    pp.Literal('ISBN10'),
    pp.Literal('ISBN')
]) + pp.Optional(':') + pp.Regex('([0-9]|-|\\s)+X?').setResultsName('isbn')

doi_parser = pp.Or([pp.Literal('DOI'), pp.Literal('doi')]) + pp.Optional(':') + \
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


def convert_pdf_to_images(pdf_path: Path, pages: int, tmpdir: Path):

    png_prefix = uuid4()
    pdf_pages = f'{pdf_path}[0-{pages - 1}]'
    args = ['convert',
            '-density',
            '300',
            '-colorspace',
            'Gray',
            '-background',
            'white',
            '-alpha',
            'off',
            pdf_pages,
            f'{tmpdir}/{png_prefix}.png']

    result = subprocess.run(args, capture_output=True)
    result.check_returncode()

    png_paths = [tmpdir / f'{png_prefix}-{i}.png' for i in range(pages)]

    return png_paths


def ocr_page_metadata(page_path: Path):

    text_file = page_path.parent / page_path.name.replace('.png', '.txt')
    args = [
        'tesseract',
        '--dpi',
        '300',
        str(page_path),
        str(text_file).replace('.txt', '')
    ]

    subprocess.run(args, capture_output=True)
    with open(text_file) as f:
        text = f.read()

    return text
