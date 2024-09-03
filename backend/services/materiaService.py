from repositories.materiaRepository import MateriaRepository
from schemas.materia import MateriaCreate
from models.materiaModel import Materia
from services.baseServiceClass import BaseClassService
from db.database import Session


class MateriaService(BaseClassService):
    def __init__(self, db: Session):
        super().__init__(db)
        self._materiaRepository = MateriaRepository(db)
    def get_all_materias(self) -> list[Materia]:
        return self._materiaRepository.get_materias()
    
    def get_materia(self, id_materia: int) -> Materia:
        return self._materiaRepository.get_materia_by_id(id_materia)
    
    def create_materia(self, materia = MateriaCreate) -> Materia:
        return self._materiaRepository.create_materia(materia)
