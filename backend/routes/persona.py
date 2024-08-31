from fastapi import APIRouter, Depends, status,HTTPException
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate
from crud import alter_persona, create_persona, get_persona_by_id, get_personas
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
    personas = get_personas(db,skip=skip,limit=limit)
    if not personas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='not found')
    return paginate(personas)

@router_personas.get(
    "/{id}", 
    response_model=Persona, 
    status_code=status.HTTP_200_OK,
    summary="Get an specific Persona by persona_id",
    )
def get_persona(persona_id:int , db: Session = Depends(get_db)):
    persona = get_persona_by_id(persona_id,db)
    if not persona:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Persona no encontrada')
    return persona


@router_personas.post(
    '/register', 
    status_code=status.HTTP_201_CREATED,
    summary="Register a new persona",
    )
def register_persona(user: PersonaCreate, db: Session = Depends(get_db)):
    response =  create_persona(db, user)
    return response


@router_personas.put(
    '/update/{id_persona}', 
    response_model=PersonaUpdate,
    status_code=status.HTTP_200_OK,
    summary="Edit a Persona and also Delete It",
    description="This endpoint was made for two purposes , you can edit a Persona by its id and you can delete it modifying the active field as False . This last feature were made for protecting the data integrity of the database",
    )
def update_persona(id_persona: int, persona_update: PersonaUpdate, db: Session = Depends(get_db)):
    response = alter_persona(db,id_persona,persona_update)
    if response :
        return response
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Persona not found")