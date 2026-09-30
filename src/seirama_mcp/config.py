import os
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(PROJECT_ROOT / ".env")

@dataclass(frozen=True)
class Settings:
    db_host: str = os.getenv("DB_HOST", "localhost")
    db_port: int = int(os.getenv("DB_PORT", "8123"))
    db_username: str = os.getenv("DB_USERNAME", "admin")
    db_password: str = os.getenv("DB_PASSWORD", "admin")
    db_name: str = os.getenv("DB_NAME", "seirama")

settings = Settings()
