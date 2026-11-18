import sqlite3
from pathlib import Path

class Connection:

    def connection():
        DATABASE_PATH = Path(__file__).parent/"data-labflow.db"
        return sqlite3.connect(DATABASE_PATH)