#blog/routers/authentication.py
from fastapi import APIRouter, Depends, HTTPException, status #type: ignore
from package.schemas import Login
from package import models, database, hashing, token
from sqlalchemy.orm import Session #type:ignore
from datetime import timedelta
import datetime
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 
from typing import Annotated

router = APIRouter(tags=['authentication'])
get_db = database.get_db

@router.post('/login')
def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not hashing.Hash.verify(user.password,request.password):
        raise HTTPException(status_code=404, detail=f"Incorrect Password")
    
    
    access_token = token.create_access_token(data = {'sub': user.email})
    return {"access_token": access_token, "token_type": 'bearer'}




