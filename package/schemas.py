#blog/schemas.py
from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title: str
    body: str
    
class Blog(BlogBase):
    class config():
        orm_mode = True



class User(BaseModel):
    name: str
    email: str
    password: str

    class config():
        orm_mode = True


class ShowUser(BaseModel):
    name:str
    email:str
    blogs: List[Blog] = []
    
    class config():
        orm_mode =True

class ShowBlog(BaseModel):

    title: str
    body: str
    author: ShowUser

    class config():
        orm_mode = True

#Authentication
class Login(BaseModel):
    username: str
    password: str



class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    email: Optional[str] = None
    