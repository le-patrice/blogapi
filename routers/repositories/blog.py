#
from fastapi import APIRouter, Depends, status, HTTPException #type: ignore
from package import schemas, database, models
from typing import List
from  sqlalchemy.orm import Session # type: ignore

get_db = database.get_db


def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs



def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy_blog(id,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with id {id} not found")
    blog.update(request,synchronize_session=False)
    db.commit()
    return 'updated successfully'



def show_blog(id,db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404,detail=f'Blog with id {id} is not available')

    return blog

