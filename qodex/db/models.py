from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, Table, Date
from sqlalchemy.orm import relationship

from qodex.db.settings import get_session

from logging import getLogger

logger = getLogger(__name__)


Base = declarative_base()

author_documents = Table('author_documents', Base.metadata,
                         Column('author_id', ForeignKey('author.id'), primary_key=True),
                         Column('document_id', ForeignKey('document.id'), primary_key=True))

document_categories = Table('document_categories', Base.metadata,
                            Column('document_id', ForeignKey('document.id'), primary_key=True),
                            Column('category_id', ForeignKey('category.id'), primary_key=True))

document_types = Table('document_types', Base.metadata,
                       Column('document_id', ForeignKey('document.id'), primary_key=True),
                       Column('document_type_id', ForeignKey('document_type.id'), primary_key=True))

shelf_documents = Table('shelf_documents', Base.metadata,
                        Column('shelf_id', ForeignKey('shelf.id'), primary_key=True),
                        Column('document_id', ForeignKey('document.id'), primary_key=True))


class Shelf(Base):

    __tablename__ = 'shelf'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(), index=True)
    description = Column(String(), index=True)

    documents = relationship('Document', secondary=shelf_documents, back_populates='shelves')

    def __str__(self):
        return str(self.name)


class Document(Base):

    __tablename__ = 'document'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    title = Column(String(), index=True)
    path = Column(String(), index=True)

    authors = relationship('Author', secondary=author_documents, back_populates='documents')
    categories = relationship('Category', secondary=document_categories, back_populates='documents',
                              order_by='asc(Category.id)')

    shelves = relationship('Shelf', secondary=shelf_documents, back_populates='documents')
    document_types = relationship('DocumentType', secondary=document_types, back_populates='documents')

    abstract = Column(String(), index=True)
    publication = Column(String(), index=True)
    edition = Column(String(), index=True)
    volume = Column(String(), index=True)
    issue = Column(String(), index=True)
    pages = Column(String(), index=True)
    date = Column(Date(), index=True)
    series = Column(String(), index=True)
    language = Column(String(), index=True)
    doi = Column(String(), index=True)
    isbn = Column(String(), index=True)
    url = Column(String(), index=True)

    def __str__(self):

        if self.title:
            return self.title
        else:
            return self.path

    @property
    def display_authors(self):

        return '; '.join(map(str, self.authors))

    @property
    def display_categories(self):

        return '; '.join(map(str, self.categories))


class DocumentType(Base):

    __tablename__ = 'document_type'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    title = Column(String(), index=True)
    description = Column(String(), index=True)

    documents = relationship('Document', secondary=document_types, back_populates='document_types')


class Author(Base):

    __tablename__ = 'author'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    first_name = Column(String(), index=True)
    last_name = Column(String(), index=True)
    middle_name = Column(String(), index=True)

    documents = relationship('Document', secondary=author_documents, back_populates='authors')

    def __str__(self):
        return '{}, {} {}'.format(self.last_name or '', self.first_name or '', self.middle_name or '')


class Category(Base):

    __tablename__ = 'category'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(), index=True)

    documents = relationship('Document', secondary=document_categories, back_populates='categories')
    parent_id = Column(Integer, ForeignKey('category.id'), index=True)
    subcategories = relationship('Category')

    def __str__(self):
        return str(self.name)

    def find_item(self, category):

        def recursive_find(cat, target):
            for item in cat.subcategories:
                if target == item:
                    return item
                else:
                    return recursive_find(item, target)
            return None

        if category == self:
            return self
        recursive_find(self, category)

    def get_ancestor_chain(self):

        ancestors = []
        session = get_session()

        def get_ancestor_chain_recursive(category):
            if category.parent_id is not None:
                parent = session.query(Category).get(category.parent_id)
                ancestors.append(parent)
                get_ancestor_chain_recursive(parent)

        get_ancestor_chain_recursive(self)

        return ancestors

    def get_descendants(self):

        descendants = []

        def get_descendants_recursive(category: Category):
            for subcategory in category.subcategories:
                descendants.append(subcategory.id)
                get_descendants_recursive(subcategory)

        get_descendants_recursive(self)

        return descendants
