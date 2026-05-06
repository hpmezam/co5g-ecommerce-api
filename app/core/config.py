from pathlib import Path
from pathlib import Path
from functools import lru_cache
from typing import Literal, Annotated

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyUrl, BeforeValidator, Field, computed_field

from app.core.validators import parse_cors

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ----------------------------
# Configuración de Base de Datos
# ----------------------------
class Settings(BaseSettings):
    # Configuración del .env
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",             # Carga automáticamente .env
        env_file_encoding='utf-8',              # Evita errores con tildes / UTF-8
        extra='ignore',                         # Ignora variables extra (no rompe la app)
        env_ignore_empty=True                   # Si una variable está vacía → no la usa
    )
    
    # ----------------------------   
    # Atributos de configuración
    # ----------------------------
    # App
    PROJECT_NAME: str = "CO5G Ecommerce API"
    DOMAIN: str = "localhost"
    ENVIRONMENT: Literal["local", "production"] = "local"
    
    # Security
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    # CORS
    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str,             # AnyURL - valida que sean URLs reales
        BeforeValidator(parse_cors)     # parse_cors - convierte string → lista
    ] = Field(default_factory=list)

    # Configuración de PostgreSQL
    POSTGRESQL_USERNAME: str
    POSTGRESQL_PASSWORD: str
    POSTGRESQL_SERVER: str = "db"
    POSTGRESQL_PORT: int = 5432
    POSTGRESQL_DATABASE: str
    
    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:   
        return (
            f"postgresql+psycopg2://{self.POSTGRESQL_USERNAME}:"
            f"{self.POSTGRESQL_PASSWORD}@"
            f"{self.POSTGRESQL_SERVER}:"
            f"{self.POSTGRESQL_PORT}/"
            f"{self.POSTGRESQL_DATABASE}"
        )

@lru_cache
def get_settings() -> Settings:
    return Settings() # type: ignore