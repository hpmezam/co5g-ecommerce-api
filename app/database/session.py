from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import get_settings

settings = get_settings()

# Crear el motor
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Crear e inicializar todas las tablas
def init_db():
    from app.database.base import Base
    Base.metadata.create_all(bind=engine)

# Dependencias para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
