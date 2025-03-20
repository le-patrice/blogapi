from fastapi import APIRouter, Depends, status, HTTPException #type: ignore
from package import schemas, database, models
from typing import List
from  sqlalchemy.orm import Session # type: ignore
from package.hashing import Hash
from .repositories import user

router = APIRouter(prefix='/user',tags=['users'])
get_db = database.get_db


#Create a user
@router.post('',response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session= Depends(get_db)):
    return user.create(request,db)


@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id: int, db:Session = Depends(get_db)):
    return user.show(id, db)
