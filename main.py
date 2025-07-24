from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welocome to my API"}


@app.get("/posts")
def get_post():
    return {"messsage: This is in get post"}