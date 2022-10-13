from fastapi import APIRouter, Response, status
from config.db import conn
from models.event import Event
from schemas.event import EventSchema
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import insert, select, update, delete
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

eventAPI = APIRouter()


#@event.get('/event', response_model=list[EventSchema], tags=["Events"])
#def get_events():
#    return conn.execute(event.select()).fetchall()  # consulta a toda la tabla


@eventAPI.post('/event', response_model=EventSchema, tags=["Events"])
def create_event(this_event: EventSchema):
    """ Create new event """

    new_event = {"name": this_event.name,
                 "event_host_id": this_event.event_host_id,
                 "event_datetime": this_event.event_datetime,
                 "location": this_event.location, 
                 "description": this_event.description,
                 "icon": this_event.icon,
                 "max_people": this_event.max_people, 
                 "participants": this_event.participants,
                 "config": this_event.config}
    # Realiza la conexion con la base de datos para insertar el nuevo usuario
    result = conn.execute(insert(Event).values(new_event))
    print("NEW EVENT . id: ", result.lastrowid)
    # Busca en la base de datos el ultimo evento creado y lo retorna para confirmar que se cre
    return conn.execute(select(Event).where(Event.id == result.lastrowid)).first()


@eventAPI.get('/event/{id}', response_model=EventSchema, tags=["Events"])
def get_event(id: str):
    """ Get event by id """

    return conn.execute(select(Event).where(Event.id == id)).first()


@eventAPI.delete('/event/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Events"])
def delete_event(id: str): 
    """ Delete event """

    # Buscar la manera de desabilitarlo no borrarlo de la base de datos directamente
    conn.execute(delete(Event).where(Event.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT) # Delete successful, no redirection needed


@eventAPI.put('/event/{id}', response_model=EventSchema, tags=["Events"])
def update_event(id: str, this_event: EventSchema):
    """ Update event """
    
    conn.execute(update(Event).values(
                 name=this_event.name, 
                 event_host_id=this_event.event_host_id,
                 event_datetime=this_event.event_datetime,
                 location=this_event.location, 
                 description=this_event.description,
                 icon=this_event.icon,
                 max_people=this_event.max_people, 
                 participants=this_event.participants,
                 config=this_event.config))
    return conn.execute(select(Event).where(Event.id == id)).first()
