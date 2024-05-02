from fastapi import FastAPI
from connection import get_db, Base, engine
from models import Base

Base.metadata.create_all(bind = engine)


app = FastAPI()


@app.get("/")
def root():
    return {"Hello" "World"}

