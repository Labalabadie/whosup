from fastapi import APIRouter, Response, status
from config.db import conn
from typing import List
from models.event import Event
from models.user import User, attending_event_rel
from schemas.event import EventSchema
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import insert, select, update, delete

eventAPI = APIRouter()



@eventAPI.get('/event', response_model=List[EventSchema], tags=["Events"])
def get_all_events():
    """ All active events """
    return conn.execute(select(Event).where(Event.status == True)).fetchall()  


@eventAPI.get('/event/inactive', response_model=List[EventSchema], tags=["Events"])
def get_inactive_events():
    """ All inactive """
    return conn.execute(select(Event).where(Event.status == False)).fetchall() 


@eventAPI.get('/event/{id}', response_model=EventSchema, tags=["Events"])
def get_event(id: int):
    """ Get event by id """
    return conn.execute(select(Event).where(Event.id == id)).first()



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
                 "config": this_event.config}
    # Realiza la conexion con la base de datos para insertar el nuevo usuario
    result = conn.execute(insert(Event).values(new_event))
    print("NEW EVENT . id: ", result.lastrowid)
    # Busca en la base de datos el ultimo evento creado y lo retorna para confirmar que se cre
    return conn.execute(select(Event).where(Event.id == result.lastrowid)).first()


@eventAPI.post('/event/{event_id}/join', tags=["Events"])
def join_event(event_id: int, user_id: int):
    """ Join event by ID """
    conn.execute(insert(attending_event_rel)
                 .values(user_id=user_id, event_id=event_id)
                 .prefix_with("IGNORE", dialect="mysql"))

    return conn.execute(select(attending_event_rel)
                        .where(attending_event_rel.c.user_id == user_id)
                        .where(attending_event_rel.c.event_id == event_id)).first()


@eventAPI.delete('/event/{event_id}/join', tags=["Events"])
def unjoin_event(event_id: int, user_id: int):
    """ Unjoin event by ID """
    conn.execute(delete(attending_event_rel)
                .where(attending_event_rel.c.user_id == user_id)
                .where(attending_event_rel.c.event_id == event_id))

    return Response(status_code=HTTP_204_NO_CONTENT)


@eventAPI.put('/event/{id}', response_model=EventSchema, tags=["Events"], response_model_exclude_unset=True)
def update_event(id: int, this_event: EventSchema):
    """ Update event """
    
    conn.execute(update(Event).values(
                 name=this_event.name, 
                 event_host_id=this_event.event_host_id,
                 event_datetime=this_event.event_datetime,
                 location=this_event.location, 
                 description=this_event.description,
                 icon=this_event.icon,
                 max_people=this_event.max_people, 
                 config=this_event.config,
                 updated_at=datetime.now()).where(Event.id == id)) # UPDATE THIS !!!!

    return conn.execute(select(Event).where(Event.id == id)).first()


@eventAPI.delete('/event/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Events"])
def delete_event(id: int): 
    """ Delete (deactivate) event """

    conn.execute(update(Event).values(
        status=False,
        updated_at=datetime.now()).where(Event.id == id))

    return Response(status_code=HTTP_204_NO_CONTENT) # Delete successful, no redirection needed