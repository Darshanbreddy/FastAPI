from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class post(BaseModel):  #creating a class called post which extends the basemodel of pydantic
    title: str          #what type
    content: str
    published: bool = True     #optional field
    rating: Optional[int]= None  #optional field deafault is none


@app.get("/")
def root():
    return {"message": "Welocome to my API"}



@app.get("/posts")
def get_post():
    return {"messsage: This is in get post"}

@app.post("/create_post")
def create_post(new_post:post):    #referencing the post calss
    print(new_post)
    print(new_post.dict())         #pydantic to dict conversion
    return {"Data": new_post}