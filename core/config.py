from pydantic import BaseSettings

class Settings(BaseSettings):
    R2_ACCOUNT_ID: str
    R2_ACCESS_KEY_ID: str
    R2_SECRET_ACCESS_KEY: str
    BUCKET_NAME: str 
    SUPABASE_KEY: str
    SUPABASE_URL: str
    FILE_BASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()