"""prepopulate document types

Revision ID: 4eeadc6f8a1f
Revises: 76a702cb0cc8
Create Date: 2022-01-22 21:07:35.545236

"""
from alembic import op
import sqlalchemy as sa
from qodex.db.models import DocumentType
from qodex.db.settings import get_session

# revision identifiers, used by Alembic.
revision = '4eeadc6f8a1f'
down_revision = '76a702cb0cc8'
branch_labels = None
depends_on = None


document_types = [
        {'title': 'article',
         'description': 'An article from a journal or magazine.',
         'display_title': 'Article'},
        {'title': 'book',
         'description': 'A book with an explicit publisher.',
         'display_title': 'Book'},
        {'title': 'booklet',
         'description': 'A work that is printed and bound, but without a named publisher or sponsoring institution.',
         'display_title': 'Booklet'},
        {'title': 'inbook',
         'description': 'A part of a book, which may be a chapter (or section or whatever) and/or a range of pages.',
         'display_title': 'Section of Book'},
        {'title': 'incollection',
         'description': 'A part of a book having its own title.',
         'display_title': 'Part of Collection'},
        {'title': 'inproceedings',
         'description': 'An article in a conference proceedings.',
         'display_title': 'Article in Conference Proceedings'},
        {'title': 'manual',
         'description': 'Technical documentation.',
         'display_title': 'Manual'},
        {'title': 'mastersthesis',
         'description': "A Master's thesis.",
         'display_title': "Master's Thesis"},
        {'title': 'misc',
         'description': 'Miscellaneous.',
         'display_title': 'Miscellaneous'},
        {'title': 'phdthesis',
         'description': 'A PhD thesis.',
         'display_title': 'PhD Thesis'},
        {'title': 'proceedings',
         'description': 'The proceedings of a conference.',
         'display_title': 'Conference Proceedings'},
        {'title': 'techreport',
         'description': 'A report published by a school or other institution, usually numbered within a series.',
         'display_title': 'Technical Report'},
        {'title': 'unpublished',
         'description': 'A document having an author and title, but not formally published.',
         'display_title': 'Unpublished'}
    ]


def upgrade():

    s = get_session(op.get_bind())
    s.bulk_insert_mappings(DocumentType, document_types)
    s.commit()


def downgrade():

    doc_type_titles = [doctype['title'] for doctype in document_types]

    s = get_session(op.get_bind())
    s.query(DocumentType).filter(DocumentType.title.in_(doc_type_titles)).delete()
    s.commit()
