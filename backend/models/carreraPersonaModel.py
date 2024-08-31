from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class CarreraPersona(Base):
    __tablename__ = "carreras_personas"
    id_carr_pers = Column(Integer, primary_key=True, index=True)
    id_persona = Column(Integer, ForeignKey("personas.id_persona"), nullable=False)
    cod_carrera = Column(Integer, ForeignKey("carreras.cod_carrera"), nullable=False)
    persona = relationship("Persona", backref="carreras_personas")
    carrera = relationship("Carrera", backref="carreras_personas")