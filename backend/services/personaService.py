from models.personaModel import Persona
from repositories.personaRepository import PersonaRepository
from schemas.persona import PersonaCreate, PersonaUpdate
from services.baseServiceClass import BaseClassService
from db.database import Session

class PersonaService(BaseClassService):
    def __init__(self, db: Session):
        super().__init__(db)
        self._personaRepository = PersonaRepository(db)
        
    def get_all_personas(self, skip:int = 0 , limit:int = 50) -> list[Persona]:
        return self._personaRepository.get_personas(skip,limit)
    
    def get_persona(self,id_persona: int) -> Persona:
        return self._personaRepository.get_persona_by_id(id_persona)
    
    def delete_persona(self,id_persona: int) -> bool:
        return self._personaRepository.delete_persona(id_persona)
    
    def update_persona(self,id_persona:int, persona_update=PersonaUpdate) -> Persona:
        return self._personaRepository.alter_persona(id_persona,persona_update)
    
    def create_persona(self,persona:PersonaCreate) -> Persona:
        return self._personaRepository.create_persona(persona)