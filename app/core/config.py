from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Manage Personal Finances and Investments"
    VERSION: str
    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Configurações de Log
    # Nível de log (ex.: debug, info, warning, error)
    LOG_LEVEL: str = "info"
    # Formato do log (ex.: text ou json)
    LOG_FORMAT: str = "json"
    # Arquivo de log
    LOG_FILE: str = "logs/app.log"

    # Campos extras
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    ALLOWED_ORIGINS: str

    class Config:
        env_file = ".env"
        # Não permite variáveis não declaradas
        extra = "forbid"


settings = Settings()
