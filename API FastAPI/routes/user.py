from datetime import datetime
from webbrowser import Grail
from config.db import conn
from cryptography.fernet import Fernet
from typing import List
from fastapi import APIRouter, Response, status
from fastapi.encoders import jsonable_encoder
from models.user import User, attending_event_rel
from models.event import Event
from models.group import Group
from models.channel import Channel
from schemas.user import UserSchema, UserSchemaDetail
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import insert, select, update, delete, join
import json

key = Fernet.generate_key()
f = Fernet(key)

userAPI = APIRouter()

# proximamente ...
#@userAPI.get('/feed/:{}', response_model=List[UserSchemaDetail], tags=["Users"])
#def get_feed():




@userAPI.get('/user', response_model=List[UserSchema], tags=["Users"])
def get_all_users():
    """ Get all active elements """
    return conn.execute(select(User).where(User.status == True)).fetchall()  # Todos los elementos activos


@userAPI.get('/user/inactive', response_model=List[UserSchema], tags=["Users"])
def get_inactive_users():
    """ All inactive """
    return conn.execute(select(User).where(User.status == False)).fetchall()


@userAPI.get('/user/{id}', response_model=UserSchema, tags=["Users"])
def get_user(id: int):
    """ Get user by id """

    return conn.execute(select(User).where(User.id == id)).first()


@userAPI.get('/user/{id}/info', response_model=UserSchema, tags=["Users"])
def get_user_info(id: int):
    """ Get detailed info of the user  events """
    public_data = conn.execute(select(User).where(User.id == id)).first()

    hosted_events = conn.execute(select(User.hosted_events, Event).join(Event).where(User.id == id)).all()
    admin_channels_list = conn.execute(select(User.admin_channels, Channel).join(Channel).where(User.id == id)).all()
    admin_groups_list = conn.execute(select(User.admin_groups, Group).join(Group).where(User.id == id)).all()

    data_dict = {column: str(getattr(public_data, column)) for column in public_data.__table__.c.keys()}
    print(data_dict)
    return public_data


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


@userAPI.put('/user/{id}', response_model=UserSchema, tags=["Users"])
def update_user(id: int, this_user: UserSchema):
    """ Update User """

    conn.execute(update(User).values(
                 name=this_user.name,
                 email=this_user.email,
                 phone=this_user.phone,
                 password=f.encrypt(this_user.password.encode("utf-8")),
                 updated_at=datetime.now()).where(User.id == id))
                 # updated_at ...
    return conn.execute(select(User).where(User.id == id)).first()


@userAPI.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(id: int):
    """ Delete (deactivate) user """

    #conn.execute(delete(User).where(User.id == id)) # <-- not delete but change to status=0 
    conn.execute(update(User).values(
        status=False,
        updated_at=datetime.now()).where(User.id == id))   # check THIS
    return Response(status_code=HTTP_204_NO_CONTENT) # Delete successful, no redirection needed
