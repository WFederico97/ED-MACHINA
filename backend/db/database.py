import os
from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv

env_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env', '.env')

if os.path.exists(env_file_path):
    print("El archivo .env fue encontrado.")
else:
    print("El archivo .env NO fue encontrado en la ruta especificada.")

load_dotenv(env_file_path)

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

if None in [DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD]:
    raise ValueError("Algunas variables de entorno no se cargaron correctamente.")

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def create_tables():
  Base.metadata.create_all(bind= engine)

def get_db() :
  db = session_local()
  try: 
    yield db
    db.commit()
  finally:
    db.close()

db_dependency = Annotated[ Session, Depends(get_db) ]