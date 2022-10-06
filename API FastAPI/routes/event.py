from fastapi import APIRouter, Response, status
from config.db import conn
from models.events import events
from schemas.event import Event
from starlette.status import HTTP_204_NO_CONTENT

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

event = APIRouter()


@event.get('/events', response_model=list[Event], tags=["Events"])
def get_events():
    return conn.execute(events.select()).fetchall()  # consulta a toda la tabla


@event.post('/events', response_model=Event, tags=["Events"])
def create_event(event: Event):
    new_event = {"event_name": event.event_name,"event_datetime": event.event_datetime,"location": event.location, "description": event.description, "participants": event.participants, "event_status": event.event_status, "nonolist": event.nonolist  }
    # Realiza la conexion con la base de datos para insertar el nuevo usuario, si devuelve un cursor en la consola es que esta bien!
    result = conn.execute(events.insert().values(new_event))
    print(result.lastrowid)
    # Ejecuta una consulta de la tabla de usuarios en donde el id de todos los usuarios coincida con el id que se acaba de guardar, solo va a traer el id que coincida. Y como devuelve una lista, con first() le digo que solamente devuelta el primero
    return conn.execute(events.select().where(events.c.id == result.lastrowid)).first()


@event.get('/events/{id}', response_model=Event, tags=["Events"])
def get_event(id: str):
    return conn.execute(events.select().where(events.c.id == id)).first()


@event.delete('/events/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Events"])
def delete_event(id: str): ## Buscar la menar de desabilitarlo no borrarlo de la base de datos directamente
    conn.execute(events.delete().where(events.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@event.put('/events/{id}', response_model=Event, tags=["Events"])
def update_event(id: str, event: Event):
    conn.execute(events.update().values(event_name=event.event_name, event_datetime=event.event_datetime, location=event.location, description=event.description, participants=event.participants ))
    return conn.execute(events.select().where(events.c.id == id)).first()
