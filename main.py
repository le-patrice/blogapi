# blog/main.py
from fastapi import (FastAPI, Depends, status,Response,HTTPException)# type: ignore
from package import  models
from package.database import engine


from routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router,)
app.include_router(blog.router,)






if __name__=="__main__":
    import uvicorn # type: ignore
    uvicorn.run("main:app",reload=True)
