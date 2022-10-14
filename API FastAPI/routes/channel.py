from fastapi import APIRouter, Response, status
from config.db import conn
from typing import List
from models.channel import Channel
from schemas.channel import ChannelSchema
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import insert, select, update, delete

channelAPI = APIRouter()


@channelAPI.get('/channel', response_model=List[ChannelSchema], tags=["Channels"])
def get_all_channels():
    return conn.execute(select(Channel)).fetchall()  # consulta a toda la tabla


@channelAPI.post('/channel', response_model=ChannelSchema, tags=["Channels"])
def create_channel(this_channel: ChannelSchema):
    """ Create group """
    
    new_channel = {"name": this_channel.name, 
                "description": this_channel.description,
                "channel_admin_id": this_channel.channel_admin_id}

    result = conn.execute(insert(Group).values(new_group)) # Realiza la conexion con la base de datos para insertar el nuevo canal
    print("NEW CHANNEL . id: ", result.lastrowid)
    # Busca en la base de datos el ultimo grupo canal y lo retorna para confirmar que se creó
    return conn.execute(select(Channel).where(Channel.id == result.lastrowid)).first()


@channelAPI.get('/channel/{id}', response_model=ChannelSchema, tags=["Channels"])
def get_channel(id: str):
    """ Get channel by id """

    return conn.execute(select(Channel).where(Channel.id == id)).first()


@channelAPI.delete('/channel/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Channels"])
def delete_channel(id: str):
    """ Delete channel """

    conn.execute(delete(Channel).where(Channel.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT) # Delete successful, no redirection needed


@channelAPI.put('/channel/{id}', response_model=ChannelSchema, tags=["Channels"])
def update_channel(id: str, this_channel: ChannelSchema):
    """ Update Channel """

    conn.execute(update(Channel).values(
                 name=this_channel.name,
                 description=this_channel.description,
                 channel_admin_id=this_channel.channel_admin_id
                 ).where(User.id == id))

    return conn.execute(select(Channel).where(Channel.id == id)).first()
