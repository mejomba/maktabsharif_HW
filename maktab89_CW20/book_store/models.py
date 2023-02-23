from database import base, engin
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text


class Book(base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    status = Column(Boolean, nullable=False, default=False)
    published = Column(Boolean, default=True)
    # created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


base.metadata.create_all(bind=engin)
