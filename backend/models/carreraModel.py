from sqlalchemy import Column, Integer, String
from db.database import Base
from sqlalchemy.orm import relationship

class Carrera(Base):
    __tablename__ = "carreras"
    cod_carrera = Column(Integer, primary_key=True, index=True)
    nombre_carrera = Column(String(50), nullable=False)
    
    personas = relationship("Persona",
                            secondary="carreras_personas",
                            back_populates="carreras")
    materias = relationship("Materia", back_populates="carrera")