from fastapi import APIRouter, Depends, status,HTTPException
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate
from services.personaService import PersonaService
from db.database import  get_db;
from schemas.persona import Persona, PersonaCreate, PersonaUpdate

router_personas = APIRouter(
  tags=['Personas'],
  prefix='/personas',
  
)

@router_personas.get(
    "/", 
    response_model=Page[Persona],
    status_code=200,
    summary="Take all personas of the DB",
)
def get_all_personas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    persona_service = PersonaService(db)
    try:
        personas = persona_service.get_all_personas(skip, limit)
        if not personas:
            raise HTTPException(404, "No personas found.")
        return paginate(personas)
    except HTTPException as e:
        raise e
    
@router_personas.get(
    "/{persona_id}", 
    response_model=Persona, 
    status_code=status.HTTP_200_OK,
    summary="Get an specific Persona by persona_id",
    )
def get_persona(persona_id:int , db: Session = Depends(get_db)):
    persona_service = PersonaService(db)
    try:
        persona = persona_service.get_persona(persona_id)
        if not persona:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Persona no encontrada')
        return persona
    except HTTPException as e:
        raise e


@router_personas.post(
    '/register', 
    status_code=status.HTTP_201_CREATED,
    summary="Register a new persona",
    )
def register_persona(persona: PersonaCreate, db: Session = Depends(get_db)):
    response =  PersonaService(db).create_persona(persona)
    return response


@router_personas.put(
    '/update/{id_persona}', 
    response_model=PersonaUpdate,
    status_code=status.HTTP_200_OK,
    summary="Edit a Persona and also Delete It",
    description="This endpoint was made for two purposes , you can edit a Persona by its id and you can delete it modifying the active field as False . This last feature were made for protecting the data integrity of the database",
    )
def update_persona(id_persona: int, persona_update: PersonaUpdate, db: Session = Depends(get_db)):
    response = PersonaService(db).update_persona(id_persona,persona_update)
    if response :
        return response
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Persona not found")