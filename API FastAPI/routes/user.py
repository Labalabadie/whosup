from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import user_data
from schemas.user import UserSchema
from starlette.status import HTTP_204_NO_CONTENT

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

userAPI = APIRouter()


#@user.get('/user', response_model=list[UserSchema], tags=["Users"])
#def get_users():
#    return conn.execute(user_data.select()).fetchall()  # consulta a toda la tabla


@userAPI.post('/user', response_model=UserSchema, tags=["Users"])
def create_user(user: UserSchema):
    new_user = {"name": user.name, "email": user.email, "phone": user.phone, 
                "created_at": "status": True, }
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    # Realiza la conexion con la base de datos para insertar el nuevo usuario, si devuelve un cursor en la consola es que esta bien!
    result = conn.execute(user_data.insert().values(new_user))
    print(result.lastrowid)
    # Ejecuta una consulta de la tabla de usuarios en donde el id de todos los usuarios coincida con el id que se acaba de guardar, solo va a traer el id que coincida. Y como devuelve una lista, con first() le digo que solamente devuelta el primero
    return conn.execute(user_data.select().where(user_data.c.id == result.lastrowid)).first()


@userAPI.get('/user/{id}', response_model=UserSchema, tags=["Users"])
def get_user(id: str):
    return conn.execute(user_data.select().where(user_data.c.id == id)).first()


@userAPI.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(id: str):
    conn.execute(user_data.delete().where(user_data.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@userAPI.put('/user/{id}', response_model=UserSchema, tags=["Users"])
def update_user(id: str, user: UserSchema):
    conn.execute(user_data.update().values(name=user.name,
                 email=user.email,phone=user.phone ,password=f.encrypt(user.password.encode("utf-8"))).where(user_data.c.id == id))
    return conn.execute(user_data.select().where(user_data.c.id == id)).first()
