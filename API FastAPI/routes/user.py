from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import User
from schemas.user import UserSchema
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import insert, select, update, delete
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

userAPI = APIRouter()


#@user.get('/user', response_model=list[UserSchema], tags=["Users"])
#def get_users():
#    return conn.execute(user_data.select()).fetchall()  # consulta a toda la tabla


@userAPI.post('/user', response_model=UserSchema, tags=["Users"])
def create_user(this_user: UserSchema):
    """ Create user """
    
    new_user = {"name": this_user.name, 
                "email": this_user.email,
                "phone": this_user.phone}

    new_user["password"] = f.encrypt(this_user.password.encode("utf-8"))
    result = conn.execute(insert(User).values(new_user)) # Realiza la conexion con la base de datos para insertar el nuevo usuario
    print("NEW USER . id: ", result.lastrowid)
    # Busca en la base de datos el ultimo usuario creado y lo retorna para confirmar que se creó
    return conn.execute(select(User).where(User.id == result.lastrowid)).first()


@userAPI.get('/user/{id}', response_model=UserSchema, tags=["Users"])
def get_user(id: str):
    """ Get user by id """

    return conn.execute(select(User).where(User.id == id)).first()


@userAPI.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(id: str):
    """ Delete user """

    conn.execute(delete(User).where(User.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT) # Delete successful, no redirection needed


@userAPI.put('/user/{id}', response_model=UserSchema, tags=["Users"])
def update_user(id: str, this_user: UserSchema):
    """ Update User """

    conn.execute(user_data.update().values(
                 name=this_user.name,
                 email=this_user.email,
                 phone=this_user.phone,
                 password=f.encrypt(this_user.password.encode("utf-8"))).where(User.id == id))
    return conn.execute(select(User).where(User.id == id)).first()
