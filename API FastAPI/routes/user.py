from datetime import datetime
from config.db import conn, Session, sess
from cryptography.fernet import Fernet
from fastapi import APIRouter, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.user import User
from models.user_rel import attending_event_rel, contact_rel
from models.event import Event
from models.group import Group
from models.channel import Channel
from models.util import unpack, unpack_many
from schemas.user import UserSchema, UserSchemaDetail, UserSchemaCreation
from schemas.event import EventSchema
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from sqlalchemy import insert, select, update, delete, join, inspect, and_, or_, not_
from typing import List

key = Fernet.generate_key()
f = Fernet(key)

userAPI = APIRouter()

# proximamente ...
#@userAPI.get('/feed/:{}', response_model=List[UserSchemaDetail], tags=["Users"])
#def get_feed():

# QUERIES -------------------


# FEED ----------------------
@userAPI.get('/user/{id}/feed', response_model=List[EventSchema], tags=["Users"])
def get_feed(id: int):
    """ get feed of specified user """
    #query = sess.query(Event).join(User, Event.participants, isouter=True).filter(not_(or_(Event.event_host_id == id, User.id == id)))
    #events_feed = query.all()

    events_feed = conn.execute(select(Event)
                                .where(~Event.participants.any(attending_event_rel.c.user_id==id))      
                                .filter(not_(Event.event_host_id == id))
                                .where(Event.status == True)).all()                                     

    print(len(events_feed))

    hosted_events_list = conn.execute( # One to many relationship join query
                        select(User.hosted_events, Event) 
                        .join(Event)
                        .where(User.id == id)).all()

    attending_events_list = conn.execute( # Many to many relationship join query
                        select(attending_event_rel, Event)
                        .join(Event, attending_event_rel.c.event_id == Event.id)
                        .where(attending_event_rel.c.user_id == id)).all()

    dic = {}                    # Response dictionary
    dic["events_feed"] = []     # Main events feed, List of events
    #dic["my_events"] = {}      # To be used in Topbar with my events, hosted and attending

    for i, row in enumerate(events_feed):
        dic["events_feed"].append({})
        for key in Event.attrs():
            dic["events_feed"][i][key] = getattr(row, key)

    dic["hosted_events"] = []
    for i, row in enumerate(hosted_events_list):
        dic["hosted_events"].append({})
        for key in Event.attrs():
            dic["hosted_events"][i][key] = getattr(row, key)

    dic["attending_events"] = []
    for i, row in enumerate(attending_events_list):
        dic["attending_events"].append({})
        for key in Event.attrs():
            dic["attending_events"][i][key] = getattr(row, key)
    
    return JSONResponse(jsonable_encoder(dic))


# GET -----------------------
@userAPI.get('/user/{id}/info', response_model=UserSchemaDetail, tags=["Users"])
def get_user_info(id: int):
    """ Get detailed info of the user """
    public_data = conn.execute(select(User).where(User.id == id)).first()
    if public_data is None:
        return Response(status_code=HTTP_404_NOT_FOUND)

    hosted_events_list = conn.execute(select(User.hosted_events, Event) # One to many relationship join query
                                    .join(Event)
                                    .where(User.id == id)).all()
                            
    attending_events_list = conn.execute(select(attending_event_rel, Event) # Many to many relationship join query
                    .join(Event, attending_event_rel.c.event_id == Event.id)
                    .where(attending_event_rel.c.user_id == id)).all()

    """contacts_list = conn.execute( # Many to many relationship join query
        select(contact_rel, User)
        .join(User, contact_rel.c.user_id == User.id)
        .where(contact_rel.c.user_id == id)).all()

    in_contacts_of_list = conn.execute(
        select(contact_rel)
        .where(contact_rel.c.contact_id == id)
        .with_entities(contact_rel.c.user_id)).all()"""

    admin_channels_list = conn.execute(select(User.admin_channels, Channel).join(Channel).where(User.id == id)).all()
    admin_groups_list = conn.execute(select(User.admin_groups, Group).join(Group).where(User.id == id)).all()

    dic = {}
    for key in User.attrs():
            dic[key] = public_data.__getattribute__(key)

    """ these loops parse only needed attrs from the relational query response """
    dic["hosted_events"] = []
    for i, row in enumerate(hosted_events_list):
        dic["hosted_events"].append({})
        for key in Event.attrs():
            dic["hosted_events"][i][key] = getattr(row, key)

    dic["attending_events"] = []
    for i, row in enumerate(attending_events_list):
        dic["attending_events"].append({})
        for key in Event.attrs():
            dic["attending_events"][i][key] = getattr(row, key)

    """dic["contacts"] = []
    for i, row in enumerate(contacts_list):
        dic["contacts"].append({})
        for key in User.attrs(): # This gets the format from the list of attrs
            dic["contacts"][i][key] = getattr(row, key)

    dic["in_contacts_of"] = []
    for elem in in_contacts_of_list:
        dic["in_contacts_of"].append(elem)"""

    return JSONResponse(jsonable_encoder(dic))

@userAPI.get('/user/{id}', response_model=UserSchema, tags=["Users"])
def get_user(id: int):
    """ Get user by id """
    return conn.execute(select(User).where(User.id == id)).first() or Response(status_code=HTTP_404_NOT_FOUND)


@userAPI.get('/user', response_model=List[UserSchema], tags=["Users"])
def get_all_users():
    """ Get all active elements """
    return conn.execute(select(User).where(User.status == True)).fetchall()  # Todos los elementos activos


@userAPI.get('/user/inactive', response_model=List[UserSchema], tags=["Users"])
def get_inactive_users():
    """ All inactive """
    return conn.execute(select(User).where(User.status == False)).fetchall()


# CREATE, UPDATE, DELETE ----
@userAPI.post('/user', response_model=UserSchemaCreation, tags=["Users"], response_model_exclude_defaults=True)
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
    return conn.execute(select(User).where(User.id == id)).first()


@userAPI.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(id: int):
    """ Delete (deactivate) user """

    #conn.execute(delete(User).where(User.id == id)) # <-- not delete but change to status=0 
    conn.execute(update(User).values(
        status=False,
        updated_at=datetime.now()).where(User.id == id))   # check THIS
    return Response(status_code=HTTP_204_NO_CONTENT) # Delete successful, no redirection needed


# CONTACTS ------------------
@userAPI.post('/user/{user_id}/contacts/add', tags=["Users"])
def add_contact(user_id: int, contact_id: int):
    """ add contact """

    resp = conn.execute(select(contact_rel) # Check for preexisting rel
                        .where(and_(contact_rel.c.user_id == user_id,
                                    contact_rel.c.contact_id == contact_id))).first()
    if resp is not None:
        return Response(status_code=HTTP_409_CONFLICT)
    
    conn.execute(insert(contact_rel).values(user_id=user_id,
                                            contact_id=contact_id))


@userAPI.get('/user/{user_id}/contacts', tags=["Users"])
def get_user_contacts(user_id: int):
    """ get list of all contacts_id for a user """
    resp = conn.execute(select(contact_rel.c.contact_id)
                        .where(contact_rel.c.user_id == user_id)).all()

    return [x.values()[0] for x in resp] or Response(status_code=HTTP_404_NOT_FOUND)

@userAPI.get('/user/{user_id}/contacts/info', tags=["Users"])
def get_user_contacts_info(user_id: int):
    """ get list of all contacts with details for a user """
    resp = conn.execute(select(User, contact_rel)
                        .join(User, contact_rel.c.contact_id==User.id)
                        .where(contact_rel.c.user_id == user_id)).all()

    return resp or Response(status_code=HTTP_404_NOT_FOUND)