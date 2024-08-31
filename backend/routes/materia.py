from fastapi import APIRouter, Depends, status,HTTPException
from sqlalchemy.orm import Session
from crud import create_materia, get_materia_by_id, get_materias
from db.database import get_db;
from schemas.materia import  MateriaCreate, Materia

router_materias = APIRouter(
  tags=['Materias'],
  prefix='/materias'
)

@router_materias.get(
    "/", 
    response_model=list[Materia],
    status_code=status.HTTP_200_OK,
    summary="Take all materias of the DB"
    )
def get_all_materias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    materias = get_materias(db,skip=skip,limit=limit)
    if not materias:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='not found')
    return materias

@router_materias.get(
    "/{id}", 
    response_model=Materia, 
    status_code=status.HTTP_200_OK,
    summary="Take a specific materia by id of the DB"
    )
def get_materia(materia_id:int , db: Session = Depends(get_db)):
    materias = get_materia_by_id(materia_id,db)
    if not materias:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='not found')
    return materias

@router_materias.post(
    '/register', 
    status_code=status.HTTP_201_CREATED,
    summary="Register a new materia",
    )
def register_materia(materia: MateriaCreate, db: Session = Depends(get_db)):
    response =  create_materia(db, materia)
    return response