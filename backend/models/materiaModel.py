from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class Materia(Base):
    __tablename__ = "materias"
    cod_materia = Column(Integer, primary_key=True, index=True)
    nombre_materia = Column(String(50), nullable=False)
    cod_carrera = Column(Integer, ForeignKey("carreras.cod_carrera"), nullable=False)
    carrera = relationship("Carrera", back_populates="materias")