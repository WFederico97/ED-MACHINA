from db.database import Session
class BaseClassService:
    def __init__(self, db: Session):
        self.db = db