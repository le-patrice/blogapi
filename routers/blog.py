from fastapi import APIRouter, Depends, status, HTTPException #type: ignore
from package import schemas, database,  oauth2
from typing import List
from  sqlalchemy.orm import Session # type: ignore
from .repositories import blog


router = APIRouter(prefix='/blog', tags=['blogs'])
get_db = database.get_db
get_current_user = oauth2.get_current_user


@router.get('',response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db),get_current_user: schemas.User = Depends(get_current_user),status=status.HTTP_200_OK):
    return blog.get_all(db)


@router.post('',status_code=201)
def create(request: schemas.Blog, db: Session = Depends(get_db),get_current_user: schemas.User = Depends(get_current_user),status=status.HTTP_200_OK):
    return blog.create_blog(request, db)

@router.delete('/{id}',status_code=204)
def destroy(id,db: Session = Depends(get_db),get_current_user: schemas.User = Depends(get_current_user),status=status.HTTP_200_OK):
    return blog.destroy_blog(id, db)

@router.put('/{id}',status_code=202)
def update(id, request: schemas.Blog, db: Session = Depends(get_db),get_current_user: schemas.User = Depends(get_current_user),status=status.HTTP_200_OK):
    return blog.update_blog(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id,db: Session=Depends(get_db),get_current_user: schemas.User = Depends(get_current_user),status=status.HTTP_200_OK):
    return blog.show_blog(id, db)


