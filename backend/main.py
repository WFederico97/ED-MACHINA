from fastapi import FastAPI
from db.database import  create_tables;
from fastapi_pagination import  add_pagination
from routes.carrera import router_carreras
from routes.materia import router_materias
from routes.persona import router_personas

app = FastAPI()
create_tables()

app.include_router(router_personas)
app.include_router(router_carreras)
app.include_router(router_materias)

@app.get("/")
def read_root():
    return {"hello" : "World"}


add_pagination(app)