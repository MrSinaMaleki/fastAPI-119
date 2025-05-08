from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

base = declarative_base()

class Author(base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    books = relationship("Book", back_populates="author")


class Book(base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,index=True)
    published_year = Column(Integer)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="Books")


