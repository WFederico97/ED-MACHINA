from db.database import Session
class BaseClassRepository:
    def __init__(self, db: Session):
        self.db = db