from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

pymysql.install_as_MySQLdb()

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost/db_list"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:HAG5C6GgF2cbA1ded1g3GH3622FEae6E@monorail.proxy.rlwy.net:25483/railway"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def criar_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()