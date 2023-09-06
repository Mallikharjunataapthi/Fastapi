
from fastapi import HTTPException,status
from  .. hashing import Hash
from .. import models


def create(request,db):
    hashpassword = Hash.bcryptpass(request.password)
    new_user = models.Users(name = request.name, email = request.email, password= hashpassword)
    db.add(new_user)
    db.commit() 
    db.refresh(new_user)
    return new_user

def getuser(id,db):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} is not Found')
    return user