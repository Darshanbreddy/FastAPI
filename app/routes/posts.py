from .. import models,schemas
from ..database import  get_db
from fastapi import status, Response, Depends, HTTPException, APIRouter
from typing import  List
from sqlalchemy.orm import Session 

router=APIRouter(
    prefix="/posts",
    tags=['users']
)



@router.get("/",response_model=List[schemas.post])
def get_posts(db: Session = Depends(get_db)):
    posts=db.query(models.Post).all()     
    return posts



@router.post("/", response_model=schemas.post)
def create_post(new_post:schemas.postcreate,db: Session = Depends(get_db)):    #referencing the post calss
   
    newpost=models.Post(**new_post.dict())       #Unpacking the dic so that it automatically assigns the value
    db.add(newpost)       
    db.commit()           #Similar to conn.commit()
    db.refresh(newpost)   #similar to adding RETURNING*

    return newpost

@router.get("/{id}", response_model=schemas.post)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if post is None:
        raise HTTPException(status_code=404, detail=f"Post with ID {id} not found")

    return post
    
    
@router.delete("/{id}")
def delete_posts(id: int, response: Response,db: Session = Depends(get_db)):
    
   
    deleted= db.query(models.Post).filter(models.Post.id==id)


    if deleted.first():
        deleted.delete(synchronize_session=False)
        db.commit()
        return {"message": "deleted"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Post with ID {id} not found"}


@router.put("/{id}", response_model=schemas.post)
def update_post(id: int, updated_post: schemas.postcreate, db: Session = Depends(get_db)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=404, detail=f"Post with ID {id} not found")

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()