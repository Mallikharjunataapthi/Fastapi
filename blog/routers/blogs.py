from typing import List
from fastapi import APIRouter,Depends, status
from sqlalchemy.orm import Session
from .. import schemas,database,oauth2
from .. Repository  import blog
router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)
get_db = database.get_db
 
@router.get('/', response_model = List[schemas.Bolgprivate])
def All(db:Session = Depends(get_db),current_user:schemas.Users = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db:Session = Depends(get_db),current_user:schemas.Users = Depends(oauth2.get_current_user)):
    return blog.create(request,db)

#get blog by Id
@router.get('/{id}', status_code=200, response_model=schemas.Bolgprivate) 
def singleBlog(id:int,db:Session = Depends(get_db),current_user:schemas.Users = Depends(oauth2.get_current_user)):
    return blog.single(id,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT) 
def deleteBlog(id:int, db:Session = Depends(get_db),current_user:schemas.Users = Depends(oauth2.get_current_user)):
    return blog.deleteitem(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def updateblog(id:int, request:schemas.Blog,db:Session = Depends(get_db),current_user:schemas.Users = Depends(oauth2.get_current_user)): 
    return blog.update(id,request,db)