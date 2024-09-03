from fastapi import APIRouter, Depends, status, HTTPException
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session
from services.carreraService import CarreraService
from db.database import  get_db
from schemas.carrera import Carrera, CarreraCreate

router_carreras = APIRouter(
  tags=['Carreras'],
  prefix='/carreras'
)

@router_carreras.get(
    "/", 
    response_model=Page[Carrera],
    status_code=status.HTTP_200_OK,
    summary="Take all carreras of the DB"
    )
def getAll(db: Session = Depends(get_db)):
    carreras_service = CarreraService(db)
    try:
        carreras = carreras_service.get_all_carrera()
        if not carreras:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Carreras not found')
        return paginate(carreras)
    except HTTPException as e:
        raise e

@router_carreras.get(
    "/{id_carrera}", 
    response_model=Carrera,
    status_code=status.HTTP_200_OK,
    summary="Take a specific carrera of the DB"
    )
def get_by_id(id_carrera: int, db: Session = Depends(get_db)):
    carreras_service = CarreraService(db)
    try:
        carreras = carreras_service.get_carrera(id_carrera)
        if not carreras:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Carrera not found')
        return carreras
    except HTTPException as e:
        raise e

@router_carreras.post(
    '/register', 
    status_code=status.HTTP_201_CREATED,
    summary="Register a new carrera",
    )
def register_carrera(carrera: CarreraCreate, db: Session = Depends(get_db)):
    response =  CarreraService(db).create_carrera(carrera)
    return response