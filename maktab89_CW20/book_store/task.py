from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
from sqlalchemy.exc import IntegrityError
from fastapi.encoders import jsonable_encoder
from database import get_db
from sqlalchemy.orm import Session
import models
from schema import Book
import json


app = FastAPI()


@app.get('/book')
def get_book(db: Session = Depends(get_db)):
    all_books = db.query(models.Book).all()
    json_data = jsonable_encoder(all_books)
    return {"books": json_data}


@app.post('/book')
def create_book(payload: Book, db: Session = Depends(get_db)):
    new_book = models.Book(**payload.dict())
    try:
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='data conflict')
    json_data = jsonable_encoder(new_book)
    return {'book': json_data}


@app.get('/book/{id}')
def get_book_id(id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if book:
        json_data = jsonable_encoder(book)
        return {"book": json_data}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='book not found')


@app.put('/book/{id}',)
def update_book(payload: Book, id: int, db: Session = Depends(get_db)):
    book_query = db.query(models.Book).filter(models.Book.id == id)
    book = book_query.first()
    if book:
        book_query.update(payload.dict())
        db.commit()
        db.refresh(book)
        json_data = jsonable_encoder(book)
        return {"update book": json_data}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} not found')


@app.delete('/book/{id}')
def delete_book(id: int, db: Session = Depends(get_db)):
    book_query = db.query(models.Book).filter(models.Book.id == id)
    book = book_query.first()
    if book:
        book_query.delete()
        db.commit()
        return {'data': 'book removed'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='book not found')


if __name__ == "__main__":
    uvicorn.run(f'{__name__}:app', reload=True)
