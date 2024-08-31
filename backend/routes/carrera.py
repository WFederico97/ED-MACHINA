from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from crud import  create_carrera, get_carreras
from db.database import  get_db
from schemas.carrera import Carrera, CarreraCreate

router_carreras = APIRouter(
  tags=['Carreras'],
  prefix='/carreras'
)

@router_carreras.get(
    "/", 
    response_model=list[Carrera],
    status_code=status.HTTP_200_OK,
    summary="Take all carreras of the DB"
    )
def getAll(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    carreras = get_carreras(db,skip=skip,limit=limit)
    if not carreras:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='not found')
    return carreras

@router_carreras.post(
    '/register', 
    status_code=status.HTTP_201_CREATED,
    summary="Register a new carrera",
    )
def register_carrera(user: CarreraCreate, db: Session = Depends(get_db)):
    response =  create_carrera(db, user)
    return response