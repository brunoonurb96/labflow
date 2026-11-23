class ExamRepository:

    def __init__(self,connection):
        self.connection = connection

    def register_exam_repo(self, exam):
        
        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO exams (name, sample_type)
        VALUES (?,?)
        """,(exam.name,
             exam.sample))

        self.connection.commit()

    def search_id_repo(self, id):

        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT id_exam as Código, name as Nome, sample_type as Tipo_de_amostra FROM exams WHERE id_exam = ?
        """, (id,))

        return cursor.fetchone()

    def search_all_repo(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT id_exam as Código, name as Nome, sample_type as Tipo_de_amostra FROM exams 
        """)
        exams = cursor.fetchall()

        for exam in exams:
            print(dict(exam))
        return exams
    
    def update_name_repo(self, id, name):

        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE exams
        SET name = ?
        WHERE id_exam = ?
        """,(name, id,))

        self.connection.commit()

    def update_sample_repo(self, id, sample):

        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE exams
        SET sample_type = ?
        WHERE id_exam = ?
        """, (sample, id,))

        self.connection.commit()
