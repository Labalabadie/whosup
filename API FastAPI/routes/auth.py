from datetime import datetime, timedelta
from config.db import conn
from cryptography.fernet import Fernet
from fastapi import APIRouter, Response
from models.user import User#, contact_rel
from starlette.status import HTTP_404_NOT_FOUND
from sqlalchemy import select
#Token
from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from typing import Union

key = Fernet.generate_key()
f = Fernet(key)

authAPI = APIRouter()

# TOKEN ---------------------


SECRET_KEY = "c6b0b513b0a069ff5362938dddd4b7bdceeba6144e64b26c6769514ea880a7c9"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



##Authorization
@authAPI.get('/user/{email}/email',tags=["Authorization"])
def get_user_email(email: str):
    """ Get user by email"""
    print("HOLA")
    response = conn.execute(select(User).where(User.email == email)).first()
    
    print(response)
    return response or Response(status_code=HTTP_404_NOT_FOUND)


@authAPI.post('/user/verifypw', tags=["Authorization"], response_model_exclude_defaults=True)
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


@authAPI.post('/user/passwordh', tags=["Authorization"], response_model_exclude_defaults=True)
def get_password_hash(password):
    return pwd_context.hash(password)

@authAPI.get('/user/auth', tags=["Authorization"], response_model_exclude_defaults=True)
#def authenticate_user(this_user: UserSchemaAuth):
 #   this_user = {"email": this_user.email,
  #              "password": this_user.password}
def authenticate_user(email: str, password: str):
    user = get_user_email(email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
    
    

