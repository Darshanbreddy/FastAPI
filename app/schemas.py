from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# class post(BaseModel):  #creating a class called post which extends the basemodel of pydantic
#     title: str          #what type
#     content: str
#     published: bool = True     #optional field
#     #rating: Optional[int]= None  #optional field deafault is none

# class create_post(BaseModel):  
#     title: str          
#     content: str
#     published: bool = True 

# class update_post(BaseModel):  
#     title: str          
#     content: str
#     published: bool         #No default value we want the user ot provide all the values wj=hile updating

class postbase(BaseModel):
    title: str
    content: str
    published: bool= True

class postcreate(postbase):
    pass 

class post(postbase):         #this is for the response model
    # title: str              #inherites these three from postbase class, adding created at only for te response model
    # content: str
    # published: bool
    created_at: datetime         

    class Config:               #pydantic only works on dict so we are converting the sqlalchemy to dict here
        orm_model= True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class Userout(BaseModel):
    id: int
    email: EmailStr

    class Config:               #pydantic only works on dict so we are converting the sqlalchemy to dict here
        orm_model= True

class Userlogin(BaseModel):
    email: EmailStr
    password: str

class token(BaseModel):
    access_token:str
    token_type: str

class token_data(BaseModel):
    id: Optional[str] = None