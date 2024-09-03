from models.materiaModel import Materia
from repositories.baseClassRepository import BaseClassRepository
from schemas.materia import MateriaCreate

class MateriaRepository(BaseClassRepository):
    def get_materias(self) -> list[Materia]:
        materias = self.db.query(Materia).all()
        return materias
    
    def get_materia_by_id(self, id_materia: int)-> Materia:
        materia = self.db.query(Materia).filter(Materia.cod_carrera == id_materia).first()
        return materia
    
    def create_materia(self, materia:MateriaCreate) -> Materia:
        new_materia = Materia(**materia.model_dump())
        self.db.add(new_materia)
        self.db.commit()
        self.db.refresh(new_materia)
        return new_materia
    