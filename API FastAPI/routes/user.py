from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import users
from schemas.user import User
from starlette.status import HTTP_204_NO_CONTENT

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()


@user.get('/users', response_model=list[User], tags=["Users"])
def get_users():
    return conn.execute(users.select()).fetchall()  # consulta a toda la tabla


@user.post('/users', response_model=User, tags=["Users"])
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email, "phone": user.phone}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    # Realiza la conexion con la base de datos para insertar el nuevo usuario, si devuelve un cursor en la consola es que esta bien!
    result = conn.execute(users.insert().values(new_user))
    print(result.lastrowid)
    # Ejecuta una consulta de la tabla de usuarios en donde el id de todos los usuarios coincida con el id que se acaba de guardar, solo va a traer el id que coincida. Y como devuelve una lista, con first() le digo que solamente devuelta el primero
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get('/users/{id}', response_model=User, tags=["Users"])
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@user.put('/users/{id}', response_model=User, tags=["Users"])
def update_user(id: str, user: User):
    conn.execute(users.update().values(name=user.name,
                 email=user.email,phone=user.phone ,password=f.encrypt(user.password.encode("utf-8"))).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()
