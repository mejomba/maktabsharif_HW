from datetime import datetime

from database import base, engin
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text, DateTime


class Task(base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    status = Column(Boolean, nullable=False, default=False)
    published = Column(Boolean, default=True)
    # create_at = Column(DateTime, default=datetime.now())
    # created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


base.metadata.create_all(bind=engin)
