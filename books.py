from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import random
from typing import Optional, Literal, List, Annotated
from uuid import uuid4

#  This is what u run in the uvicorn app
app = FastAPI()

#BOOK MODEL - Pydantic

class Book(BaseModel):
    name: str
    author: str
    price: float
    genre: Literal["fiction", "non-fiction"]
    book_id: Optional[str] = uuid4().hex


BOOK_DATABASE  = []

# / -> Root for health checks
@app.get("/")
async def home():
    return {"message": "Welcome, to my BookStore!"}


# /list-books -> for showing all the books
@app.get("/list-books")
async def list_books():
    return {"books": BOOK_DATABASE}


# PATH PARAMETER
# /book-by-index/{index} -> /book-by-index/0 - for searching a particular book
@app.get("/book-by-index/{index}")
async def book_by_index(index: int):
    if index < 0 or index >= len(BOOK_DATABASE):
        #FAIL
        raise HTTPException(404, f"Index {index} is out of range {len(BOOK_DATABASE)}")
    else:    
        book = BOOK_DATABASE[index]
        return {"book": book}


# /get-random-book
@app.get("/get-random-book")
async def get_random_book():
    return {"book" : random.choice(BOOK_DATABASE)}

# The POST BODY
# /add-book
@app.post("/add-book")
async def add_book(book: Book):
    book.book_id = uuid4().hex
    BOOK_DATABASE.append(book)
    return {"message": f"The book {book.name} with book_id: {book.book_id} was added successfully"}

# QUERY PARAMETER
# /get-book?id=...
@app.get("/get-book")
async def get_book(book_id: str):
    for book in BOOK_DATABASE:
        if book_id == book.book_id:
            return book
    
    raise HTTPException(404, f"The book with id: {book_id} could not be found in the database.")