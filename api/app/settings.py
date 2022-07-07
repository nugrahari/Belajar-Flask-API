import os
from typing import Optional

from pydantic import BaseSettings

from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
	DEBUG: bool = os.getenv('DEBUG') == True

	class JWT:
		SECRET: Optional[str] = os.getenv('JWT_SECRET')
		ISSUER: Optional[str] = os.getenv('JWT_ISSUER')
	

	class DB:
		HOST: str = os.getenv('SRS_DB_HOST')
		DB: Optional[str] = os.getenv('SRS_DB') if os.getenv('TEST') is None else 'srs_test'
		USER: Optional[str] = os.getenv('SRS_USER') if os.getenv('TEST') is None else 'srs_test'
		PASSWORD: Optional[str] = os.getenv('SRS_PASSWORD') if os.getenv('TEST') is None else 'srs_test'
		PORT: str = os.getenv('SRS_DB_PORT')


settings: Settings = Settings()