from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:1@localhost/learn_fastapi'
SQLALCHEMY_DATABASE_URL = "sqlite:///book.db"

engin = create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engin)
base = declarative_base()

# base.metadata.create_all(bind=engin)


def get_db():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()
