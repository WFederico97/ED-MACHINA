from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class Persona(Base):
    __tablename__ = 'personas'
    id_persona = Column(Integer, primary_key=True, index=True)
    nombre_persona = Column(String(50), nullable=False)
    apellido_persona = Column(String(50), nullable=False)
    email_persona = Column(String(50), unique=True, nullable=False)
    active = Column(Boolean, default=True)  #If we want to delete a persona , the better way is giving an active falso just for not affecting to the data integrity rules
    carreras = relationship("Carrera",
                            secondary="carreras_personas",
                            back_populates="personas")