from typing import List, Optional
from pydantic import BaseModel
from schemas.carrera import Carrera

class PersonaBase(BaseModel):
    nombre_persona: str
    apellido_persona: str
    email_persona: str

class PersonaCreate(PersonaBase):
    carreras: Optional[List[int]] = []
    active: Optional[bool] = True


class Persona(PersonaBase):
    id_persona: int
    active: bool 
    carreras: List[Carrera] = []
    class Config:
        orm_mode = True

class PersonaUpdate(BaseModel):
    nombre_persona: Optional[str] = None
    apellido_persona: Optional[str] = None
    email_persona: Optional[str] = None
    carreras: Optional[List[int]] = None
    active: Optional[bool] = True