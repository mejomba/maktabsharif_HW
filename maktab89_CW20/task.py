from typing import Dict, List

from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
from database import get_db
from sqlalchemy.orm import Session
import models
from schema import Task, Task2


app = FastAPI()


@app.get('/task', response_model=List[Task2])
def get_task(db: Session = Depends(get_db)):
    all_tasks = db.query(models.Task).all()
    print(type(all_tasks))
    # return 'hello'
    return all_tasks


@app.post('/task', response_model=Task)
def create_task(payload: Task, db: Session = Depends(get_db)):
    new_task = models.Task(**payload.dict())
    try:
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
    except Exception:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='data conflict')
    return new_task


@app.get('/task/{id}')
def get_task_id(id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    if task:
        return {"task": task}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='task not found')


@app.put('/task/{id}',)
def update_task(payload: Task, id: int, db: Session = Depends(get_db)):
    task_query = db.query(models.Task).filter(models.Task.id == id)
    task = task_query.first()
    if task:
        task_query.update(payload.dict())
        db.commit()
        db.refresh(task)
        return {"update task": task}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} not found')


@app.delete('/task/{id}')
def delete_task(id: int, db: Session = Depends(get_db)):
    task_query = db.query(models.Task).filter(models.Task.id == id)
    task = task_query.first()
    if task:
        task_query.delete()
        db.commit()
        return {'data': 'task removed'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='task not found')


if __name__ == "__main__":
    uvicorn.run(f'{__name__}:app', reload=True)
