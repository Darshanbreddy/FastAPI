from fastapi import FastAPI,status, Response, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session 
from . import models
from .database import engine, get_db


models.Base.metadata.create_all(bind=engine)
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


post_creation=[{"title":"My book", "content":"good book", "id":1}]


class post(BaseModel):  #creating a class called post which extends the basemodel of pydantic
    title: str          #what type
    content: str
    published: bool = True     #optional field
    rating: Optional[int]= None  #optional field deafault is none


@app.get("/")
def root():
    return {"message": "Welocome to my API"}



@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts """)  #running the sql 
    posts= cursor.fetchall()                    #fetching all the info from database
    return {"data": posts}

@app.post("/posts")
def create_post(new_post:post):    #referencing the post calss
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",(new_post.title, new_post.content, new_post.published))  
    newpost= cursor.fetchone()
    con.commit()
    return {"Data": newpost}

@app.get("/posts/{id}")         #id field here is a path parameter
def get_post(id:int, response: Response):   #converting it into a int because sting might also be passed which is not id

    cursor.execute("""SELECT * from posts WHERE id= %s """,(str(id)))  #converting back to a string so that we do not get error int doesn't support indexing
    post = cursor.fetchone()

    if post:
        return {"data": post}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Post with ID {id} not found"}
    
@app.delete("/posts/{id}")
def delete_posts(id: int, response: Response):
    
    cursor.execute("""DELETE from posts WHERE id= %s RETURNING * """,(str(id)))  #converting back to a string so that we do not get error int doesn't support indexing
    deleted=cursor.fetchone()
    con.commit()


    if deleted:
        return {"message": "deleted"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Post with ID {id} not found"}


@app.put("/posts/{id}")
def update_post(id: int, updated_post: post, response: Response):
    cursor.execute(""" UPDATE posts set title=%s, content=%s, published=%s WHERE id=%s RETURNING *""",(updated_post.title, updated_post.content, updated_post.published, str(id) ))
    update= cursor.fetchone()
    con.commit()

    if update:
        return {"message": "Updated"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Post with ID {id} not found"}

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return {"status" : "Success"}
 