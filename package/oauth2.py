from fastapi import Depends, HTTPException, status #type:ignore
from package import token as tk
from fastapi.security import OAuth2PasswordBearer #type:ignore


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail=f'Could not validate credentials',
        headers = {'WWW-Authenticate': 'Bearer'},
    )
    return tk.verify_token(token, credentials_exception)
