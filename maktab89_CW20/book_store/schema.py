from pydantic import BaseModel
from typing import Optional


class Book(BaseModel):
    title: str
    content: str
    status: Optional[bool] = False
    published: Optional[bool] = True
