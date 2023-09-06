from datetime import timedelta
from fastapi import APIRouter,Depends, HTTPException,status
from .. routers.jwttoken import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from sqlalchemy.orm import Session
from .. import models,database
from .. hashing import Hash

from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter( 
    tags=['Authentication']
)
get_db = database.get_db
@router.post('/login')
def Login(request : OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.name == request.username).first();
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')
    
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Password')
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
 
