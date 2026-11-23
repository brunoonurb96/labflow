import sqlite3
class PatientRepository:
    def __init__(self, connection):
        self.connection = connection

    def register_patient_repo(self,patient):

        cursor = self.connection.cursor()

        cursor.execute("""
        INSERT INTO patient (cpf, name, birthdate, address, phone)
        VALUES (?,?,?,?,?)
        """,(patient.cpf,
             patient.name,
             patient.birth,
             patient.address,
             patient.phone
             )
        )
        self.connection.commit()

    def search_cpf_repo(self,cpf):

        cursor = self.connection.cursor()
        cursor.execute("SELECT cpf as CPF, name as Nome, birthdate as Data_de_nascimento, address as Endereço, phone as Telefone FROM patient WHERE cpf = ?",(cpf,))

        return cursor.fetchone()
        
    
    def search_all(self):
        
        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT cpf as CPF, name as Nome, birthdate as Data_de_nascimento, address as Endereço, phone as Telefone FROM patient
        """)

        patients = cursor.fetchall()

        for patient in patients:
            print(dict(patient))

        return patients 

    def update_name_repo(self,cpf,name):
      
        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE patient 
        SET name = ?
        WHERE cpf = ?
        """, (name,
             cpf,
        ))  
        self.connection.commit()

    def update_birth_repo(self, cpf, birth):

        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE patient
        SET birthdate = ?
        WHERE cpf = ?
        """, (birth, cpf,))
        
        self.connection.commit()

    def update_address_repo(self, cpf, address):

        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE patient
        SET address = ?
        WHERE cpf = ?
        """, (address, cpf,))

        self.connection.commit()

    def update_phone_repo(self, cpf, phone):

        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE patient
        SET phone = ?
        WHERE cpf = ?
        """, (phone, cpf,))

        self.connection.commit()

    