from database.tables_creation import * 
from repositories.patient_repository import *
from repositories.exam_repository import *
from repositories.sample_repository import *
from services.patient_service import *
from services.exam_service import *
from services.sample_service import *

TablesCreation.tables()

conn = Connection.connection()
exam_conn = ExamRepository(conn)
exam_serv = ExamService(exam_conn)
patient_repository = PatientRepository(conn)
patient_serv = PatientService(patient_repository)
sample_repository = SampleRepository(conn)
sample_serv = SampleService(sample_repository, patient_serv, exam_serv)

def register_samp():
    cpf = input("Insira o CPF do cliente: ")
    exam = input("Insira o exame que será feito: ")
    date = input("Insira a data da coleta: ")

    sample_serv.register_sample_serv(cpf, exam, date)

def update_samp():
    while True:
        print("===============================")
        print(" Menu Alterar Amostra Coletada")
        print("===============================")
        
        try:
            option = int(input("""O que deseja alterar?
1. CPF da amostra
2. Exame da amostra
3. Data coletada
4. Status
    
5. Voltar ao menu anterior
"""))
            if option == 1:
                id = input("Digite o código da amostra: ")
                sample_serv.search_id_serv(id, SampleService.update_cpf_serv)
                return True
            
            if option == 2:
                id = input("Digite o código da amostra: ")
                sample_serv.search_id_serv(id, SampleService.update_exam_serv)
                return True
            
            if option == 3:
                id = input("Digite o código da amostra: ")
                sample_serv.search_id_serv(id, SampleService.update_date_serv)
                return True
            
            if option == 4:
                id = input("Digite o código da amostra: ")
                sample_serv.search_id_serv(id, SampleService.update_status_serv)
                return True
                        
            if option == 5:
                return True
            if option <= 0 or option > 5:
                raise ValueError
        except ValueError:
            print("Erro: Insira um número de 1 a 5 apenas")
                

def samples():
    while True:
        print("=====================")
        print("     Menu Amostras     ")
        print("=====================")
        
        try:
            option = int(input("""
1. Cadastrar amostra coletada
2. Alterar amostra
3. Buscar apenas uma amostra
4. Buscar todas as amostras
5. Buscar amostras por CPF
    
6. Voltar ao  menu anterior
"""))
            if option == 1:
                register_samp()
            if option == 2:
                update_samp()
            if option == 3:
                id = input("Digite o código da amostra: ")
                sample_serv.search_one_show(id)
            if option == 4:
                sample_serv.search_all_serv()
            if option == 5:
                cpf = input("Digite o CPF correspondente as amostra: ")
                sample_serv.search_cpf_serv(cpf)
            if option == 6:
                return True
            if option <= 0 or option > 5:
                raise ValueError
        except ValueError:
            print("Erro: Insira um número de 1 a 5 apenas")


def update_exam():
    while True:
        print("=====================")
        print(" Menu Alterar Exame")
        print("=====================")
    
        try:
            option = int(input("""O que deseja alterar?
1. Nome do exame
2. Tipo de amostra

3. Voltar ao menu anterior
"""))
            if option == 1:
                id = input("Digite o código do exame: ")
                exam_serv.search_exam_id(id, ExamService.update_exam_name)
                return True
            
            if option == 2:
                id = input("Digite o código do exame: ")
                exam_serv.search_exam_id(id, ExamService.update_exam_sample)
                return True
            
            if option == 3:
                return True
            if option < 0 or option > 3:
                raise ValueError
        except ValueError:
            print("Erro: Insira um número de 1 a 3 apenas")          

def register_ex():
    name = input("Digite o nome do exame: ")
    sample_type = input("Digite o tipo de amostra do exame: ")

    exam_serv.register_exam(name, sample_type)

def exams():
    while True:
        print("=====================")
        print("     Menu Exames     ")
        print("=====================")

        try:
            option = int(input("""
1. Cadastrar exame
2. Alterar exame
3. Buscar apenas um exame
4. Buscar todos os exames

5. Voltar ao  menu anterior
"""))
            if option == 1:
                register_ex()
            if option == 2:
                update_exam()
            if option == 3:
                id = input("Digite o código do exame: ")
                exam_serv.search_one_show(id)
            if option == 4:
                exam_serv.search_all()
            if option == 5:
                return True
            if option <= 0 or option > 5:
                raise ValueError
        except ValueError:
            print("Erro: Insira um número de 1 a 5 apenas")

def update_pat():
    while True:
        print("=====================")
        print("Menu Alterar Paciente")
        print("=====================")

        try:
            option = int(input("""O que deseja alterar?
1. Nome
2. Data de nascimento
3. Endereço
4. Telefone

5. Voltar ao menu anterior
"""))
            if option == 1:
                cpf = input("Digite o cpf do paciente: ")
                patient_serv.search_cpf(cpf, PatientService.update_pat_name)
                return True
            
            if option == 2:
                cpf = input("Digite o cpf do paciente: ")
                patient_serv.search_cpf(cpf, PatientService.update_pat_birth)
                return True
                
            if option == 3:
                cpf = input("Digite o cpf do paciente: ")
                patient_serv.search_cpf(cpf, PatientService.update_pat_address)
                return True
            
            if option == 4:
                cpf = input("Digite o cpf do paciente: ")
                patient_serv.search_cpf(cpf, PatientService.update_pat_phone)
                return True
            
            if option == 5:
                return True
            
            if option <= 0 or option > 5:
                raise ValueError
            
        except ValueError:
            print("Erro: Insira um número de 1 a 5 apenas")


def register_pat():
    cpf = input("Insira o CPF do paciente: ")
    name = input("Inisira o nome do paciente: ")
    birth = input("Insira uma data de nascimento para esse paciente (Formato AAAA-MM-DD)")
    address = input("Insira um endereço para esse paciente: ")
    phone = input("Insira um telefone para esse paciente, apenas números: ")

    patient_serv.register_patient(cpf, name, birth, address, phone)

def patients():
    
    while True:
        print("=====================")
        print("   Menu Pacientes"    )
        print("=====================")

        try:
            option = int(input("""
1. Cadastrar Paciente
2. Alterar Paciente
3. Buscar apenas um paciente
4. Buscar todos os pacientes

5. Voltar ao menu anterior
"""))
            if option == 1:
                register_pat()

            if option == 2:
                update_pat()

            if option == 3:
                cpf = input("Digite o cpf do paciente: ")
                patient_serv.search_one_show(cpf)

            if option == 4:
                patient_serv.search_all_serv()

            if option == 5:
                return True
            if option <= 0 or option > 5:
                raise ValueError
        except ValueError:
            print("Erro: Insira um número de 1 a 5 apenas")
def main():
    while True:
        print("=====================")
        print("   Menu principal"    )
        print("=====================")
        try:
            option = int(input("""
1. Pacientes
2. Exames
3. Amostras

4. Sair
"""))
        
            if option == 1:
                patients()
            if option == 2:
                exams()
            if option == 3:
                samples()
            if option == 4:
                print("Encerrando...")
                break
            if option <= 0 or option > 4:
                raise ValueError
        except ValueError:
            print("Erro: Insira um número de 1 a 4 apenas")
       
if __name__ == "__main__":
    main()

