from fastapi import APIRouter, Response, status
from config.db import conn
from models.group import Group
from schemas.group import GroupSchema
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import insert, select, update, delete
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

groupAPI = APIRouter()


#@user.get('/user', response_model=list[UserSchema], tags=["Users"])
#def get_users():
#    return conn.execute(user_data.select()).fetchall()  # consulta a toda la tabla


@groupAPI.post('/group', response_model=GroupSchema, tags=["Groups"])
def create_group(this_group: GroupSchema):
    """ Create group """
    
    new_group = {"name": this_group.name, 
                "description": this_group.description,
                "group_admin_id": this_group.group_admin_id}

    result = conn.execute(insert(Group).values(new_group)) # Realiza la conexion con la base de datos para insertar el nuevo grupo
    print("NEW GROUP . id: ", result.lastrowid)
    # Busca en la base de datos el ultimo grupo creado y lo retorna para confirmar que se creó
    return conn.execute(select(Group).where(Group.id == result.lastrowid)).first()


@groupAPI.get('/group/{id}', response_model=GroupSchema, tags=["Groups"])
def get_group(id: str):
    """ Get group by id """

    return conn.execute(select(Group).where(Group.id == id)).first()


@groupAPI.delete('/group/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Groups"])
def delete_group(id: str):
    """ Delete group """

    conn.execute(delete(Group).where(Group.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT) # Delete successful, no redirection needed


@groupAPI.put('/group/{id}', response_model=GroupSchema, tags=["Groups"])
def update_group(id: str, this_group: GroupSchema):
    """ Update Group """

    conn.execute(update(Group).values(
                 name=this_group.name,
                 description=this_group.description,
                 group_admin_id=this_group.group_admin_id
                 ).where(Group.id == id))

    return conn.execute(select(Group).where(Group.id == id)).first()
