import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    RABBITMQ_URL = os.getenv("RABBITMQ_URL")
    MONGODB_URL = os.getenv("MONGODB_URL")
    POSTGRESQL_URL = os.getenv("POSTGRESQL_URL")
    print(POSTGRESQL_URL)
    ORACLE_URL = os.getenv("ORACLE_URL")

settings = Settings()