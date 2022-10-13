from fastapi import FastAPI
from routes.user import userAPI
from routes.event import eventAPI
from fastapi.middleware.cors import CORSMiddleware
from config.db import meta, engine

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8100",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(userAPI)
app.include_router(eventAPI)
meta.create_all(engine)
