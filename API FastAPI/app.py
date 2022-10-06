<<<<<<< HEAD
from fastapi import FastAPI
from routes.user import user
from routes.event import event
from fastapi.middleware.cors import CORSMiddleware


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

app.include_router(user)
=======
from fastapi import FastAPI
from routes.user import user
from routes.event import event

app = FastAPI()

app.include_router(user)
>>>>>>> 2f9ef4324d3b07ca3809107279c7e760baae2a72
app.include_router(event)