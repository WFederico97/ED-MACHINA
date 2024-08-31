from typing import List, Optional
from pydantic import BaseModel


class MateriaBase(BaseModel):
    nombre_materia: str

class MateriaCreate(MateriaBase):
    cod_carrera: int
    pass

class Materia(MateriaBase):
        cod_materia: int
        class Config:
            orm_mode = True