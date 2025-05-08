from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database, schemas

app = FastAPI()

# starting db and tables
database.init_db()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/authors/", response_model=schemas.AuthorRead)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_author = models.Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


@app.get("/authors/", response_model= list[schemas.AuthorRead])
def read_authors(db: Session = Depends(get_db)):
    return db.query(models.Author).all()



# Books

@app.post("/books/", response_model=schemas.BookRead)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):

    if not db.query(models.Author).get(book.author_id):
        raise HTTPException(status_code=404, detail="author not found")

    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=list[schemas.BookRead])
def read_books(db:Session = Depends(get_db)):
    return db.query(models.Book).all()



@app.get("/books/{book_id}", response_model=schemas.BookRead)
def read_book(book_id:int, db:Session = Depends(get_db)):
    book = db.query(models.Book).get(book_id)

    if not book:
        raise HTTPException(status_code=404, detail="book not found")

    return book




