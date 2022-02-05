from pathlib import Path
from qodex.db.models import Author, Document
from typing import List, Tuple


def rename(pattern: str, document: Document, file_ext: str = '.pdf'):

    format_dict = {}
    authors = document.authors
    categories = document.categories

    if '{last_name}' in pattern and len(authors) > 0:
        format_dict['last_name'] = authors[0].last_name
    if '{first_name}' in pattern and len(authors) > 0:
        format_dict['first_name'] = authors[0].first_name
    if '{author}' in pattern:
        if len(authors) > 0:
            format_dict['author'] = str(authors[0]).strip()
        else:
            format_dict['author'] = ''
    if '{authors_last_names}' in pattern:
        format_dict['authors_last_names'] = ', '.join([auth.last_name for auth in authors])
    if '{authors}' in pattern:
        format_dict['authors'] = '; '.join([str(auth).strip() for auth in authors])
    if '{title}' in pattern:
        format_dict['title'] = document.title
    if '{categories}' in pattern:
        format_dict['categories'] = ', '.join([str(cat).strip() for cat in categories])

    new_file_name = pattern.format(**format_dict)
    if not Path(new_file_name).suffix in {file_ext, file_ext.upper()}:
        new_file_name += file_ext
    location = Path(document.path).parent
    new_location = location / new_file_name

    return new_location
