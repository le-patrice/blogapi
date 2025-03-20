#Blog/routers/respositories/user.py
from fastapi import APIRouter, Depends, status, HTTPException #type: ignore
from  sqlalchemy.orm import Session # type: ignore
from package.hashing import Hash
from package import schemas,database, models
get_db = database.get_db


#Create a user

def create(request: schemas.User, db: Session= Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



def show(id: int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} is not available")
    
    return user

