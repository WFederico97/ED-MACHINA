from models.carreraModel import Carrera
from repositories.baseClassRepository import BaseClassRepository
from schemas.carrera import CarreraCreate

class CarreraRepository(BaseClassRepository):
    def get_carreras(self) -> list[Carrera]:
        carreras = self.db.query(Carrera).all()
        return carreras
    
    def get_carrera_by_id(self, id_carrera: int)-> Carrera:
        carrera = self.db.query(Carrera).filter(Carrera.cod_carrera == id_carrera).first()
        return carrera
    
    def create_carrera(self, carrera:CarreraCreate) -> Carrera:
        new_carrera = Carrera(**carrera.model_dump())
        self.db.add(new_carrera)
        self.db.commit()
        self.db.refresh(new_carrera)
        return new_carrera