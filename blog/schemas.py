from pydantic import BaseModel

from typing import List


class BaseBlog(BaseModel):
    class Config():
        orm_mode = True
class Blog(BaseBlog):
    title:str
    body:str 

#create
class Users(BaseModel):
    name:str
    email:str
    password:str

class hideUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog] = []

    class Config():
        orm_mode = True



class Bolgprivate(BaseModel):
    #we can add the column names which need to be dispay in response
    title:str
    body:str
    creator:hideUser

    class Config():
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str