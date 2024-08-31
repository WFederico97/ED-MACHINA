
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas.carrera import Carrera,CarreraCreate
from schemas.materia import Materia, MateriaCreate
from schemas.persona import Persona,PersonaCreate, PersonaUpdate
from models import Persona, Materia, Carrera, CarreraPersona




############ Personas ################
#                                    #
######################################
def get_personas(db: Session, skip:int = 0, limit:int = 50):
    query = select(Persona).filter(Persona.active == True).offset(skip).limit(limit)
    result = db.execute(query)
    personas = result.scalars().all()
    return personas

def get_persona_by_id(persona_id: int, db: Session):
    query = select(Persona).filter(Persona.id_persona == persona_id, Persona.active == True)
    result = db.execute(query)
    persona = result.scalar_one_or_none()
    
    if persona is None:
        raise HTTPException(404, f"The persona with the id:{persona_id} was deactivated or not found. Contact administrator for more info.")
    
    persona.carreras = [
        carrera for carrera in db.query(Carrera)
        .join(CarreraPersona, Carrera.cod_carrera == CarreraPersona.cod_carrera)
        .filter(CarreraPersona.id_persona == persona_id).all()
    ]
    
    return persona


def create_persona(db:Session, persona: PersonaCreate):
    new_persona = Persona(**persona.model_dump(exclude={'carreras'}))
    db.add(new_persona)
    db.commit()
    db.refresh(new_persona)
    
    if persona.carreras:
        for carrera_id in persona.carreras:
            db.add(CarreraPersona(id_persona=new_persona.id_persona, cod_carrera=carrera_id))
        db.commit()
    return {'msg': f'La persona con id: {new_persona.id_persona} fue registrada correctamente'}

def alter_persona( db: Session, id_persona: int, persona_update: PersonaUpdate):
    persona = db.query(Persona).filter(Persona.id_persona == id_persona).first()
    if persona:
        updated_fields = {}

        if persona_update.nombre_persona is not None and persona.nombre_persona != persona_update.nombre_persona:
            persona.nombre_persona = persona_update.nombre_persona
            updated_fields['nombre_persona'] = persona_update.nombre_persona

        if persona_update.apellido_persona is not None and persona.apellido_persona != persona_update.apellido_persona:
            persona.apellido_persona = persona_update.apellido_persona
            updated_fields['apellido_persona'] = persona_update.apellido_persona

        if persona_update.email_persona is not None and persona.email_persona != persona_update.email_persona:
            persona.email_persona = persona_update.email_persona
            updated_fields['email_persona'] = persona_update.email_persona
            
        if persona_update.active is not None and persona.active != persona_update.active:
            persona.active = persona_update.active
            updated_fields['active'] = persona_update.active

        if persona_update.carreras is not None:
            updated_carreras = []
            for cod_carrera in persona_update.carreras:
                carrera = db.query(Carrera).filter(Carrera.cod_carrera == cod_carrera).first()
                if carrera:
                    if carrera not in persona.carreras:
                        persona.carreras.append(carrera)
                        updated_carreras.append(carrera.cod_carrera)
                    else:
                        raise HTTPException(status_code=400, detail=f'La persona ya se encuentra inscripta a la carrera: {carrera.nombre_carrera}')
            if updated_carreras:
                updated_fields['carreras'] = updated_carreras

        db.commit()
        db.refresh(persona)

        return PersonaUpdate(**updated_fields)
    
def delete_persona(db: Session, id_persona: int):
    persona = db.query(Persona).filter(Persona.id_persona == id_persona).first()
    if not persona:
        raise HTTPException(status_code=404, detail="Persona not found")

    if not persona.activo:
        raise HTTPException(status_code=400, detail="Persona already inactive")

    #Set as active = False for logic erasering of the persona
    persona.activo = False
    db.commit()
    db.refresh(persona)

    return persona


############ Carreras ################
#                                    #
######################################

def get_carreras(db:Session, skip:int = 0, limit:int = 50):
    query = select(Carrera).offset(skip).limit(limit)
    result = db.execute(query)
    carreras = result.scalars().all()
    return carreras

def get_carrera_by_id(db:Session, carrera_id: int):
    query = select(Carrera).filter(Carrera.cod_carrera == carrera_id)
    result = db.execute(query)
    carrera = result.scalar_one_or_none()
    return carrera

def create_carrera(db:Session, carrera: CarreraCreate):
    new_carrera = Carrera(**carrera.model_dump())
    db.add(new_carrera)
    db .commit()
    db.refresh(new_carrera)
    
    return {'msg': f'La carrera: {new_carrera.nombre_carrera} fue registrada correctamente'}


############ Materias ################
#                                    #
######################################
def get_materias(db:Session, skip:int = 0, limit:int = 50):
    query = select(Materia).offset(skip).limit(limit)
    result = db.execute(query)
    materias = result.scalars().all()
    return materias

def get_materia_by_id(db:Session, materia_id: int):
    query = select(Materia).filter(Carrera.cod_materia == materia_id)
    result = db.execute(query)
    carrera = result.scalar_one_or_none()
    return carrera

def create_materia(db:Session, materia: MateriaCreate):
    new_materia = Materia(**materia.model_dump())
    db.add(new_materia)
    db.commit()
    db.refresh(new_materia)
    
    return {'msg': f'La carrera: {new_materia.nombre_materia} fue registrada correctamente'}