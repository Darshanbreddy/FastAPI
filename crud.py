from fastapi import FastAPI,status, Response
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

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
    return {"data": post_creation}

@app.post("/posts")
def create_post(new_post:post):    #referencing the post calss
    new_id = post_creation[-1]['id'] + 1 if post_creation else 1
    post_dict = new_post.dict()         #to dict from pydantic
    post_dict['id'] = new_id            #assigning id
    post_creation.append(post_dict)     # Append to the list   
    return {"Data": new_post}

@app.get("/posts/{id}")         #id field here is a path parameter
def get_post(id:int, response: Response):
    for post in post_creation:
        if post["id"] == id:
            return {"data": post}
    response.status_code= status.HTTP_404_NOT_FOUND
    return {"error": f"Post with ID {id} not found"}
    
@app.delete("/posts/{id}")
def delete_posts(id: int, response: Response):
    for post in post_creation:
        if post["id"] == id:
            post_creation.remove(post)
            return {"Message": f"Post with ID {id} deleted"}
    
    response.status_code= status.HTTP_404_NOT_FOUND
    return {"error": f"Post with ID {id} not found"}


@app.put("/posts/{id}")
def update_post(id: int, updated_post: post, response: Response):
    for index, post in enumerate(post_creation):
        if post["id"] == id:
            # Convert updated_post to dict and keep the same ID
            post_dict = updated_post.dict()
            post_dict["id"] = id
            post_creation[index] = post_dict
            return {"message": f"Post with ID {id} updated", "data": post_dict}

    response.status_code = status.HTTP_404_NOT_FOUND
    return {"error": f"Post with ID {id} not found"}
