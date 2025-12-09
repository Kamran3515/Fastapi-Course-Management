from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://fastapiuser:fastapipass@db:5432/fastapi_courses"

settings = Settings()

