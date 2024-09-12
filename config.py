from pydantic import BaseSettings


class Settings(BaseSettings):
    EMAIL: str
    EMAIL_PASSWORD: str
    EMAIL_HOST: str
    EMAIL_PORT: int
    DATABASE_MONGO_URL: str


    class Config:
        env_file = './.env'


settings = Settings()
