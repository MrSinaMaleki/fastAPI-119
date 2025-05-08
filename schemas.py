from pydantic import BaseModel

class AuthorCreate(BaseModel):
    name: str

class AuthorRead(AuthorCreate):
    id: int

    class Config:
        orm_mode = True


class BookCreate(BaseModel):
    title: str
    published_year: int
    author_id : int


class BookRead(BookCreate):
    id: int
    author: AuthorRead

    class Config:
        orm_mode = True


