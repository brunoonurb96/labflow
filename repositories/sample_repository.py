class SampleRepository:

    def __init__(self, connection):
        self.connection = connection

    def register_sample_repo(self,sample):
        
        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO sample (cpf_s, exam_s, datetime)
        VALUES (?,?,?)
        """,(sample.cpf,
             sample.exam,
             sample.date
             ))
        self.connection.commit()

    def search_id_repo(self,id):

        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT s.id_sample as Código, p.name as Paciente, p.cpf as Documento, e.name as Exame, s.datetime as Data_de_coleta, s.status as Status FROM sample AS s
        INNER JOIN patient AS p
            ON s.cpf_s = p.cpf
        INNER JOIN exams AS e
            ON s.exam_s = e.id_exam
        WHERE s.id_sample = ?""", (id,))

        return cursor.fetchone()

    def search_all_repo(self):

        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT s.id_sample as Código, p.name as Paciente, p.cpf as Documento, e.name as Exame, s.datetime as Data_de_coleta, s.status as Status FROM sample AS s
        INNER JOIN patient AS p
            ON s.cpf_s = p.cpf
        INNER JOIN exams AS e
            ON s.exam_s = e.id_exam
            ORDER BY s.id_sample
        """)

        samples = cursor.fetchall()
        
        
        return samples

    def search_cpf_repo(self, cpf):
        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT s.id_sample as Código, p.name as Paciente, p.cpf as Documento, e.name as Exame, s.datetime as Data_de_coleta, s.status as Status FROM sample AS s
        INNER JOIN patient AS p
            ON s.cpf_s = p.cpf
        INNER JOIN exams AS e
            ON s.exam_s = e.id_exam
        WHERE s.cpf_s = ?
                """,(cpf,))
        
        return cursor.fetchall()
        
        
        

    def update_cpf_repo(self, id, cpf):

        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE sample
        SET cpf_s = ?
        WHERE id_sample = ?
        """, (cpf, id,))

        self.connection.commit()
        

    def update_exam_repo(self, id, exam):

        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE sample
        SET exam_s = ?
        WHERE id_sample = ? 
        """,(exam, id,))

        self.connection.commit()

    def update_date_repo(self, id, date):

        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE sample
        SET datetime = ?
        WHERE id_sample = ?
        """,(date, id,))

        self.connection.commit()

    def update_status_repo(self, id, status):

        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE sample
        SET status = ?
        WHERE id_sample = ?
        """, (status, id,))

        self.connection.commit()
