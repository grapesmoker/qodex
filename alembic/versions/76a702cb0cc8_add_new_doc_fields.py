"""add new doc fields

Revision ID: 76a702cb0cc8
Revises: 7d4def039304
Create Date: 2021-06-14 22:27:23.742916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76a702cb0cc8'
down_revision = '7d4def039304'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('document', sa.Column('abstract', sa.String(), nullable=True))
    op.add_column('document', sa.Column('publication', sa.String(), nullable=True))
    op.add_column('document', sa.Column('edition', sa.String(), nullable=True))
    op.add_column('document', sa.Column('volume', sa.String(), nullable=True))
    op.add_column('document', sa.Column('issue', sa.String(), nullable=True))
    op.add_column('document', sa.Column('pages', sa.String(), nullable=True))
    op.add_column('document', sa.Column('date', sa.Date(), nullable=True))
    op.add_column('document', sa.Column('series', sa.String(), nullable=True))
    op.add_column('document', sa.Column('language', sa.String(), nullable=True))
    op.add_column('document', sa.Column('doi', sa.String(), nullable=True))
    op.add_column('document', sa.Column('isbn', sa.String(), nullable=True))
    op.add_column('document', sa.Column('url', sa.String(), nullable=True))
    op.add_column('document', sa.Column('full_text', sa.Text(), nullable=True))
    op.add_column('document', sa.Column('page_count', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_document_abstract'), 'document', ['abstract'], unique=False)
    op.create_index(op.f('ix_document_date'), 'document', ['date'], unique=False)
    op.create_index(op.f('ix_document_doi'), 'document', ['doi'], unique=False)
    op.create_index(op.f('ix_document_edition'), 'document', ['edition'], unique=False)
    op.create_index(op.f('ix_document_isbn'), 'document', ['isbn'], unique=False)
    op.create_index(op.f('ix_document_issue'), 'document', ['issue'], unique=False)
    op.create_index(op.f('ix_document_language'), 'document', ['language'], unique=False)
    op.create_index(op.f('ix_document_pages'), 'document', ['pages'], unique=False)
    op.create_index(op.f('ix_document_publication'), 'document', ['publication'], unique=False)
    op.create_index(op.f('ix_document_series'), 'document', ['series'], unique=False)
    op.create_index(op.f('ix_document_url'), 'document', ['url'], unique=False)
    op.create_index(op.f('ix_document_volume'), 'document', ['volume'], unique=False)
    op.create_index(op.f('ix_document_page_count'), 'document', ['page_count'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_document_volume'), table_name='document')
    op.drop_index(op.f('ix_document_url'), table_name='document')
    op.drop_index(op.f('ix_document_series'), table_name='document')
    op.drop_index(op.f('ix_document_publication'), table_name='document')
    op.drop_index(op.f('ix_document_pages'), table_name='document')
    op.drop_index(op.f('ix_document_language'), table_name='document')
    op.drop_index(op.f('ix_document_issue'), table_name='document')
    op.drop_index(op.f('ix_document_isbn'), table_name='document')
    op.drop_index(op.f('ix_document_edition'), table_name='document')
    op.drop_index(op.f('ix_document_doi'), table_name='document')
    op.drop_index(op.f('ix_document_date'), table_name='document')
    op.drop_index(op.f('ix_document_abstract'), table_name='document')
    op.drop_column('document', 'url')
    op.drop_column('document', 'isbn')
    op.drop_column('document', 'doi')
    op.drop_column('document', 'language')
    op.drop_column('document', 'series')
    op.drop_column('document', 'date')
    op.drop_column('document', 'pages')
    op.drop_column('document', 'issue')
    op.drop_column('document', 'volume')
    op.drop_column('document', 'edition')
    op.drop_column('document', 'publication')
    op.drop_column('document', 'abstract')
    op.drop_column('document', 'full_text')
    op.drop_column('document', 'page_count')
    # ### end Alembic commands ###
