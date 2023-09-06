from fastapi import APIRouter, Depends
from .. import schemas,database,oauth2
from sqlalchemy.orm import Session
from .. Repository import users
router = APIRouter(
    prefix='/users',
    tags=['Users']
)
get_db = database.get_db


@router.post('/',response_model=schemas.hideUser)
def CreateUser(request: schemas.Users,db:Session = Depends(get_db)):
    return users.create(request,db)

@router.get("/{id}",response_model=schemas.hideUser)
def get_user(id:int,db:Session = Depends(get_db),current_user:schemas.Users = Depends(oauth2.get_current_user)):
    return users.getuser(id,db)