from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:admin@localhost/fastapi'   #typeofdb://username:password@ipaddress/dbname

engine=create_engine(SQLALCHEMY_DATABASE_URL)   #responsible for establishing connection

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)   #to talk to the database we are creating a session

Base = declarative_base()

def get_db():               #getting a session to pur DB
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()