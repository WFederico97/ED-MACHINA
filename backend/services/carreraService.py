from models.carreraModel import Carrera
from repositories.carreraRepository import CarreraRepository
from schemas.carrera import CarreraCreate
from services.baseServiceClass import BaseClassService
from db.database import Session


class CarreraService(BaseClassService):
    def __init__(self, db: Session):
        super().__init__(db)
        self._carreraRepository = CarreraRepository(db)
        
    def get_all_carrera(self) -> list[Carrera]:
        return self._carreraRepository.get_carreras()
    
    def get_carrera(self, id_carrera: int) -> Carrera:
        return self._carreraRepository.get_carrera_by_id(id_carrera)
    
    def create_carrera(self, carrera:CarreraCreate) -> Carrera:
        return self._carreraRepository.create_carrera(carrera)
