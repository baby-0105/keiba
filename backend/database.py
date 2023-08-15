import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    os.environ.get('MYSQL_USER'),
    os.environ.get('MYSQL_PASSWORD'),
    os.environ.get('MYSQL_HOST'),
    os.environ.get('MYSQL_DATABASE'),
)

engine = create_engine(
    DATABASE,
    encoding='utf-8',
    echo=True
)

SessionLocal = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = SessionLocal.query_property()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
