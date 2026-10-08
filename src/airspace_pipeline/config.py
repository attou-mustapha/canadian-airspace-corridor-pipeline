import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_host: str = os.getenv("DB_HOST", "localhost")
    db_port: int = int(os.getenv("DB_PORT", "5434"))
    db_name: str = os.getenv("DB_NAME", "airspace_db")
    db_user: str = os.getenv("DB_USER", "flight_admin")
    db_password: str = os.getenv("DB_PASSWORD", "flight_secure_pwd")

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

settings = Settings()
