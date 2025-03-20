from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore


SQLALCHAMLY_DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHAMLY_DATABASE_URL,connect_args={'check_same_thread':False} )

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False,)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close
