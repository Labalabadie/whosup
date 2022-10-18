from datetime import datetime
from webbrowser import Grail
from config.db import conn
from cryptography.fernet import Fernet
from typing import List
from fastapi import APIRouter, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.user import User, attending_event_rel
from models.event import Event
from models.group import Group
from models.channel import Channel
from schemas.user import UserSchema, UserSchemaDetail
from schemas.event import EventSchema
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import insert, select, update, delete, join, inspect
import json

key = Fernet.generate_key()
f = Fernet(key)

userAPI = APIRouter()

# proximamente ...
#@userAPI.get('/feed/:{}', response_model=List[UserSchemaDetail], tags=["Users"])
#def get_feed():

def unpack(obj, attrs):
    ret = {}
    for key in attrs:
        ret[key] = getattr(obj, key)
    return ret

def unpack_many(obj, attrs):
    """ unpacks a List of Rows object into a List of Dicts
        obj = Listo of rows
        attrs = list of attributes to unpack """
    ret = []
    for i, row in enumerate(obj):
        ret.append({})
        for key in attrs:
            ret[i][key] = getattr(row, key)



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


@userAPI.get('/user/{id}/info', response_model=UserSchemaDetail, tags=["Users"])
def get_user_info(id: int):
    """ Get detailed info of the user """
    public_data = conn.execute(select(User).where(User.id == id)).first()

    # One to many relationship join query
    hosted_events_list = conn.execute(
        select(User.hosted_events, Event)
        .join(Event)
        .where(User.id == id)).all()

    # Many to many relationship
    attending_events_list = conn.execute(
        select(User.attending_events, attending_event_rel, Event)
        .join(attending_event_rel, User.id == attending_event_rel.c.user_id)
        .join(Event, attending_event_rel.c.event_id == Event.id)
        .where(User.id == id)).all()

    admin_channels_list = conn.execute(select(User.admin_channels, Channel).join(Channel).where(User.id == id)).all()
    admin_groups_list = conn.execute(select(User.admin_groups, Group).join(Group).where(User.id == id)).all()


    my_dic = {}
    for key in User.attrs():
            my_dic[key] = public_data.__getattribute__(key)

    """ this loops parses only needed attrs from the relational query response """
    my_dic["hosted_events"] = []
    for i, row in enumerate(hosted_events_list):
        my_dic["hosted_events"].append({})
        for key in Event.attrs():
            my_dic["hosted_events"][i][key] = getattr(row, key)

    my_dic["attending_events"] = []
    for i, row in enumerate(attending_events_list):
        my_dic["attending_events"].append({})
        for key in Event.attrs():
            my_dic["attending_events"][i][key] = getattr(row, key)

    return JSONResponse(jsonable_encoder(my_dic))



@userAPI.post('/user', response_model=UserSchema, tags=["Users"], response_model_exclude_defaults=True)
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
