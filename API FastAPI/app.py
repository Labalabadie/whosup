from fastapi import FastAPI, Depends, HTTPException, status
from datetime import datetime, timedelta
from models.user import User
from jose import JWTError, jwt
from routes.auth import authAPI, authenticate_user, create_access_token, SECRET_KEY, ALGORITHM
from routes.user import get_user, userAPI
from schemas.user import Token, UserSchema
from routes.event import eventAPI
from routes.group import groupAPI
from routes.channel import channelAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from config.db import meta, engine


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8100",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(userAPI)
app.include_router(authAPI)
app.include_router(eventAPI)
app.include_router(groupAPI)
app.include_router(channelAPI)

meta.create_all(engine)


ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(id, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = email
    except JWTError:
        raise credentials_exception
    user = get_user(id)
    if user is None:
        raise credentials_exception
    return user


# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#    if current_user.disabled:
#        raise HTTPException(status_code=400, detail="Inactive user")
 #   return current_user


@app.post("/token", response_model= Token, tags=["Authorization"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "Bearer"}

@app.get("/user/{id}/", response_model= UserSchema, tags=["Authorization"])
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
