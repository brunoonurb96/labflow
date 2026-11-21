import sqlite3
from pathlib import Path

class Connection:

    def connection():
        DATABASE_PATH = Path(__file__).parent/"data-labflow.db"
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row

        return conn