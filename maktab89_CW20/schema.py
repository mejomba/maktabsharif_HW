from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    title: str
    content: str
    status: Optional[bool] = False
    published: Optional[bool] = True
    # created_at: datetime

    class Config:
        orm_mode = True


class Task2(BaseModel):
    title: str
    content: str
    # status: Optional[bool] = False
    # published: Optional[bool] = True
    # created_at: datetime

    class Config:
        orm_mode = True


class TaskId(BaseModel):
    id: int