from fastapi import APIRouter, Response, status
from config.db import conn
from typing import List
from models.notification import Notification
from schemas.notification import NotificationSchema
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from sqlalchemy import insert, select, update, delete

notificationAPI = APIRouter()



@notificationAPI.get('/notification', response_model=List[NotificationSchema], tags=["Notification"])
def get_all_notification():
    """ All notifications """
    return conn.execute(select(Notification).where(Notification.status == True)).fetchall()  



@notificationAPI.get('/notification/{id}', response_model=NotificationSchema, tags=["Notification"])
def get_notification(id: int):
    """ Get notification by id """
    return conn.execute(select(Notification).where(Notification.id == id)).first()



@notificationAPI.post('/notification', response_model=NotificationSchema, tags=["Notification"])
def create_notification(this_notification: NotificationSchema):
    """ Create new notification """

    new_notification = {"text"}
    # Realiza la conexion con la base de datos para insertar el nuevo usuario
    result = conn.execute(insert(Notification).values(new_notification))
    print("NEW NOTIFICATION . id: ", result.lastrowid)
    # Busca en la base de datos el ultimo evento creado y lo retorna para confirmar que se cre
    return conn.execute(select(Notification).where(Notification.id == result.lastrowid)).first()


