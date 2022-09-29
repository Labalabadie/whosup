from fastapi import FastAPI
from routes.user import user
from routes.event import event

app = FastAPI()

app.include_router(user)
app.include_router(event)