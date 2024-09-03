from fastapi import APIRouter, Depends, status,HTTPException
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session
from services.materiaService import MateriaService
from db.database import get_db;
from schemas.materia import  MateriaCreate, Materia

router_materias = APIRouter(
  tags=['Materias'],
  prefix='/materias'
)

@router_materias.get(
    "/", 
    response_model=Page[Materia],
    status_code=status.HTTP_200_OK,
    summary="Take all materias of the DB"
    )
def get_all_materias( db: Session = Depends(get_db)):
    materias_service = MateriaService(db)
    try:
        materias = materias_service.get_all_materias()
        if not materias:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Materias not found')
        return paginate(materias)
    except HTTPException as e:
        raise e

@router_materias.get(
    "/{id_materia}", 
    response_model=Materia, 
    status_code=status.HTTP_200_OK,
    summary="Take a specific materia by id of the DB"
    )
def get_materia(id_materia:int , db: Session = Depends(get_db)):
    materias_service = MateriaService(db)
    try:
        materias= materias_service.get_materia(id_materia)
        if not materias:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Materia not found')
        return materias
    except HTTPException as e:
        raise e

@router_materias.post(
    '/register', 
    status_code=status.HTTP_201_CREATED,
    summary="Register a new materia",
    )
def register_materia(materia: MateriaCreate, db: Session = Depends(get_db)):
    response =  MateriaService(db).create_materia(materia)
    return response