from fastapi import HTTPException
from models.carreraModel import Carrera
from models.carreraPersonaModel import CarreraPersona
from models.personaModel import Persona
from repositories.baseClassRepository import BaseClassRepository
from schemas.persona import PersonaCreate, PersonaUpdate

class PersonaRepository(BaseClassRepository):
    def get_personas(self, skip:int = 0 , limit:int = 50) -> list[Persona]:
        return self.db.query(Persona).filter(Persona.active == True).offset(skip).limit(limit).all()
    
    def get_persona_by_id(self, id_persona: int) -> Persona:
        persona = self.db.query(Persona).filter(Persona.id_persona == id_persona, Persona.active == True).first()
        if persona is None:
            raise HTTPException(404,f"The persona with the id:{id_persona} was deactivated or not found. Contact administrator for more info.")
        persona.carreras = [
        carrera for carrera in self.db.query(Carrera)
        .join(CarreraPersona, Carrera.cod_carrera == CarreraPersona.cod_carrera)
        .filter(CarreraPersona.id_persona == id_persona).all()
        ]
        
        return persona
    
    def create_persona(self, persona: PersonaCreate) -> Persona:
        new_persona = Persona(**persona.model_dump(exclude={'carreras'}))
        self.db.add(new_persona)
        self.db.commit()
        self.db.refresh(new_persona)
        
        if persona.carreras:
            for carrera_id in persona.carreras:
                self.db.add(CarreraPersona(id_persona=new_persona.id_persona, cod_carrera=carrera_id))
            self.db.commit()
        return new_persona
    
    def alter_persona( self, id_persona: int, persona_update: PersonaUpdate) -> Persona:
        persona = self.db.query(Persona).filter(Persona.id_persona == id_persona).first()
        if persona:
            updated_fields = {}

            if persona_update.nombre_persona is not None and persona.nombre_persona != persona_update.nombre_persona:
                persona.nombre_persona = persona_update.nombre_persona
                updated_fields['nombre_persona'] = persona_update.nombre_persona

            if persona_update.apellido_persona is not None and persona.apellido_persona != persona_update.apellido_persona:
                persona.apellido_persona = persona_update.apellido_persona
                updated_fields['apellido_persona'] = persona_update.apellido_persona

            if persona_update.email_persona is not None and persona.email_persona != persona_update.email_persona:
                persona.email_persona = persona_update.email_persona
                updated_fields['email_persona'] = persona_update.email_persona
                
            if persona_update.active is not None and persona.active != persona_update.active:
                persona.active = persona_update.active
                updated_fields['active'] = persona_update.active

            if persona_update.carreras is not None:
                updated_carreras = []
                for cod_carrera in persona_update.carreras:
                    carrera = self.db.query(Carrera).filter(Carrera.cod_carrera == cod_carrera).first()
                    if carrera:
                        if carrera not in persona.carreras:
                            persona.carreras.append(carrera)
                            updated_carreras.append(carrera.cod_carrera)
                        elif carrera in persona.carreras:
                            raise HTTPException(status_code=400, detail=f'La persona ya se encuentra inscripta a la carrera: {carrera.nombre_carrera}')
                if updated_carreras:
                    updated_fields['carreras'] = updated_carreras

            self.db.commit()
            self.db.refresh(persona)

        return PersonaUpdate(**updated_fields)
    
    def delete_persona(self, id_persona: int) -> bool:
        persona = self.db.query(Persona).filter(Persona.id_persona == id_persona).first()
        if not persona:
            raise HTTPException(status_code=404, detail="Persona not found")

        if not persona.activo:
            raise HTTPException(status_code=400, detail="Persona already inactive")

        #Set as active = False for logic erasering of the persona
        persona.activo = False
        self.db.commit()
        self.db.refresh(persona)

        return True