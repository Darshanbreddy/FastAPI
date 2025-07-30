from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welocome to my API"}


@app.get("/posts")
def get_post():
    return {"messsage: This is in get post"}

@app.post("/create_post")
def create_post(payload: dict= Body(...)):    #extracting the message by storing it in a dict called payload and priting it later
    print(payload)
    return {f"new post, title is {payload['title']} and Content is: {payload['content']}"}