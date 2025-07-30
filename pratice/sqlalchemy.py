from fastapi import FastAPI,status, Response, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session 
from . import models, schemas
from .database import engine, get_db


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


post_creation=[{"title":"My book", "content":"good book", "id":1}]





@app.get("/")
def root():
    return {"message": "Welocome to my API"}



@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts """)  #running the sql 
    # posts= cursor.fetchall()                    #fetching all the info from database

    posts=db.query(models.Post).all()     #fetching all the posts using sqlalchemy

    return {"data": posts}


@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):

    post=db.query(models.Post).all()     #fetching all the posts using sqlalchemy

    return {"data" : post}

#####


@app.post("/posts")
def create_post(new_post:schemas.postcreate,db: Session = Depends(get_db)):    #referencing the post calss
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",(new_post.title, new_post.content, new_post.published))  
    # newpost= cursor.fetchone()
    # con.commit()

    # newpost=models.Post(title=new_post.title, content=new_post.content,published=new_post.published)
    # print(new_post.dict())    #Using pydantic to convert it into a dict so that if we have many fileds it will automatically be assigned
    newpost=models.Post(**new_post.dict())       #Unpacking the dic so that it automatically assigns the value
    db.add(newpost)       
    db.commit()           #Similar to conn.commit()
    db.refresh(newpost)   #similar to adding RETURNING*

    return {"Data": newpost}

@app.get("/posts/{id}")         #id field here is a path parameter
def get_post(id:int, response: Response,db: Session = Depends(get_db)):   #converting it into a int because sting might also be passed which is not id

    # cursor.execute("""SELECT * from posts WHERE id= %s """,(str(id)))  #converting back to a string so that we do not get error int doesn't support indexing
    # post = cursor.fetchone()

    post= db.query(models.Post).filter(models.Post.id==id).first()

    if post:
        return {"data": post}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Post with ID {id} not found"}
    
@app.delete("/posts/{id}")
def delete_posts(id: int, response: Response,db: Session = Depends(get_db)):
    
    # cursor.execute("""DELETE from posts WHERE id= %s RETURNING * """,(str(id)))  #converting back to a string so that we do not get error int doesn't support indexing
    # deleted=cursor.fetchone()
    # con.commit()
    deleted= db.query(models.Post).filter(models.Post.id==id)


    if deleted.first():
        deleted.delete(synchronize_session=False)
        db.commit()
        return {"message": "deleted"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Post with ID {id} not found"}



    # cursor.execute(""" UPDATE posts set title=%s, content=%s, published=%s WHERE id=%s RETURNING *""",(updated_post.title, updated_post.content, updated_post.published, str(id) ))
    # update= cursor.fetchone()
    # con.commit()

@app.put("/posts/{id}")
def update_post(id: int, updated_post: schemas.postcreate, response: Response, db: Session = Depends(get_db)):


    # cursor.execute(""" UPDATE posts set title=%s, content=%s, published=%s WHERE id=%s RETURNING *""",(updated_post.title, updated_post.content, updated_post.published, str(id) ))
    # update= cursor.fetchone()
    # con.commit()

    # Query the database for the post with this ID
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    # If not found, return 404
    if post is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Post with ID {id} not found"}

    # Update the post
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return {"message": "Updated successfully"}


 