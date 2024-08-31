from typing import List
from pydantic import BaseModel

from schemas.materia import Materia

class CarreraBase(BaseModel):
    nombre_carrera: str

class CarreraCreate(CarreraBase):
    pass

class Carrera(CarreraBase):
    cod_carrera: int
    materias: List[Materia] = []
    class Config:
        orm_mode = True