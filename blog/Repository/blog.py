
from fastapi import HTTPException,status
from .. import models



def get_all(db): 
    getBlogs = db.query(models.Blog).all() 
    return getBlogs

def create(request,db):
    new_blog = models.Blog(title = request.title, body = request.body,user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def single(id,db):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail=f'Data Not Found With Given Id {id}')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'response' : f'Data Not Found With Given Id {id}'}
    return blog

def deleteitem(id,db):
    delblog = db.query(models.Blog).filter(models.Blog.id == id)
    if not delblog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    delblog.delete(synchronize_session=False)
    db.commit()
    return 'done';

def update(id,request,db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not Found")
    blog.update({'title':request.title,'body':request.body})
    db.commit()
    return