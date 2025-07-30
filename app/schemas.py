from pydantic import BaseModel

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