from fastapi import APIRouter, Response, status
from config.db import conn
from models.event import event
from schemas.event import EventSchema
from starlette.status import HTTP_204_NO_CONTENT

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

eventAPI = APIRouter()


#@event.get('/event', response_model=list[EventSchema], tags=["Events"])
#def get_events():
#    return conn.execute(event.select()).fetchall()  # consulta a toda la tabla


@eventAPI.post('/event', response_model=EventSchema, tags=["Events"])
def create_event(this_event: EventSchema):
    new_event = {"event_name": this_event.event_name,"event_datetime": this_event.event_datetime,"location": this_event.location, "description": this_event.description, "participants": this_event.participants, "event_status": this_event.event_status, "nonolist": this_event.nonolist  }
    # Realiza la conexion con la base de datos para insertar el nuevo usuario, si devuelve un cursor en la consola es que esta bien!
    result = conn.execute(event.insert().values(new_event))
    print(result.lastrowid)
    # Ejecuta una consulta de la tabla de usuarios en donde el id de todos los usuarios coincida con el id que se acaba de guardar, solo va a traer el id que coincida. Y como devuelve una lista, con first() le digo que solamente devuelta el primero
    return conn.execute(event.select().where(event.c.id == result.lastrowid)).first()


@eventAPI.get('/event/{id}', response_model=EventSchema, tags=["Events"])
def get_event(id: str):
    return conn.execute(event.select().where(event.c.id == id)).first()


@eventAPI.delete('/event/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Events"])
def delete_event(id: str): ## Buscar la menar de desabilitarlo no borrarlo de la base de datos directamente
    conn.execute(event.delete().where(event.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@eventAPI.put('/event/{id}', response_model=EventSchema, tags=["Events"])
def update_event(id: str, this_event: EventSchema):
    conn.execute(event.update().values(event_name=this_event.event_name, event_datetime=this_event.event_datetime, location=this_event.location, description=this_event.description, participants=this_event.participants ))
    return conn.execute(event.select().where(event.c.id == id)).first()
