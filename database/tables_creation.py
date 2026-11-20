from database.connection import Connection

class TablesCreation:
    def tables():
        conn = Connection.connection()
        cursor = conn.cursor()
        cursor.executescript("""
        CREATE TABLE IF NOT EXISTS patient (
        cpf TEXT PRIMARY KEY ,
        name TEXT NOT NULL,
        birthdate DATE NOT NULL,
        address TEXT NOT NULL,
        phone TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS exams(
        id_exam INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sample_type TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS sample(
        id_sample INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf_s INTEGER NOT NULL,
        exam_s INTERGER NOT NULL,
        datetime DATE NOT NULL,
        status TEXT NOT NULL DEFAULT "COLETADA",

        FOREIGN KEY (cpf_s) REFERENCES patient(cpf),
        FOREIGN KEY (exam_s) REFERENCES exam(id_exam)
        )
        """)
    