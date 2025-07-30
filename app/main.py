from fastapi import FastAPI,status, Response, Depends, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session 
from . import models, schemas
from .database import engine, get_db
from . import utils
from .routes import users, posts




models.Base.metadata.create_all(bind=engine)   #to create all the models(DB)
app = FastAPI()




#Connection to our database
while True:
    try:
        con= psycopg2.connect(host='localhost', database='fastapi',user='postgres', password='admin', cursor_factory=RealDictCursor)
        cursor= con.cursor()
        print("Connection is done to database")
        break
    except Exception as error:
        print("Connection to database falled")
        print("Error : ", error)
        time.sleep(5)


app.include_router(posts.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "Welocome to my API"}





