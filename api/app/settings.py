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
		PORT: str = os.getenv('SRS_DB_PORT')
		DB: str = os.getenv('SRS_DB')
		USER: str = os.getenv('SRS_USER')
		PASSWORD: str = os.getenv('SRS_PASSWORD')








settings: Settings = Settings()