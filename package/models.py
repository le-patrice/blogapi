#blog/models.py
from sqlalchemy import Column, Integer, String, ForeignKey #type: ignore
from .database import Base
from sqlalchemy.orm import relationship #type: ignore

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    author = relationship("User",back_populates="blogs")
    user_id = Column(Integer, ForeignKey('users.id'))


class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True,index=True)
    name= Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship('Blog',back_populates="author")

