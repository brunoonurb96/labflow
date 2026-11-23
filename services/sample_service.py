from models.sample import *
from services.patient_service import *
from services.exam_service import *
class SampleService:

    def __init__(self, repository):
        self.repository = repository

    def register_sample_serv(self, cpf, exam, date):

        sample = Sample(cpf, exam, date)
        try:
            if not cpf.strip():
                raise ValueError("CPF é obrigatório, não pode estar vazio!")
            if not PatientService.patient_exists(self, cpf):
                print("Não existe paciente cadastrado com esse CPF")
                return
            if not ExamService.exam_exists(self,exam):
                print("Não existe exame cadastrado com esse código!")
                return
            if not exam.strip():
                raise ValueError("Exame é obrigatório, não pode estar vazio!")
            if not date.strip():
                raise ValueError("Data de coleta é obrigatório, não pode estar vazio!")
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Data de nascimento tem que estar em formato AAAA-MM-DD")       
        except ValueError as e:
            print(f"Erro: {e}")
            return
        self.repository.register_sample_repo(sample)
        print("Amostra cadastrada com sucesso!")
    
    def search_id_serv(self,id, callback):
        if self.repository.search_id_repo(id):
            return callback(self,id)
        else:
            print("Nenhuma amostra coletada com esse código!")

    def search_one_show(self, id):
        iden = self.repository.search_id_repo(id)
        if not iden:
            print("Nenhuma amostra coletada com esse código!")
        else:
            return print(dict(iden))

    def search_cpf_serv(self, cpf):
        iden = self.repository.search_cpf_repo(cpf)
        if not iden:
            print("Nenhuma amostra coletada com esse CPF")
            return False
        else:
            for cpf in iden:
                print(dict(cpf))
            return True
    
    def search_all_serv(self):
        idens = self.repository.search_all_repo()
        for iden in idens:
            print(dict(iden))
        return True

    def update_cpf_serv(self, id):
        
        new_cpf = Sample.update_samp_cpf(self)
        try:
            if not new_cpf.strip():
                raise ValueError("CPF é obrigatório, não pode estar vazio!")
            if PatientService.patient_exists(self, new_cpf):
                self.repository.update_cpf_repo(id, new_cpf)
            else:    
                print("Não existe paciente cadastrado com esse CPF")
                return False
        except ValueError as e:
            print(f"Erro: {e}")
            return
        print("Amostra atualizado com sucesso!")
        return True

    def update_exam_serv(self,id):
        
        new_exam = Sample.update_samp_exam(self)
        try:
            if not new_exam.strip():
                raise ValueError("Exame é obrigatório, não pode estar vazio!")
            if ExamService.exam_exists(self,new_exam):
                self.repository.update_exam_repo(id, new_exam)
            else:
                print("Não existe exame cadastrado com esse código!")
                return False
        except ValueError as e:
            print(f"Erro: {e}")
            return
        print("Amostra atualizado com sucesso")
        return True

    def update_date_serv(self, id):

        new_date = Sample.update_samp_date(self)
        try:
            if not new_date.strip():
                raise ValueError("Data de coleta é obrigatório, não pode estar vazio!")
            try:
                datetime.strptime(new_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Data de nascimento tem que estar em formato AAAA-MM-DD")
        except ValueError as e:
            print(f"Erro: {e}")
            return
        self.repository.update_date_repo(id, new_date)

    def update_status_serv(self, id):

        new_status = Sample.update_samp_status(self)
        new_status = new_status.upper()
        try:
            if not new_status.strip():
                raise ValueError("Status é obrigatório, não pode estar vazio!")
        except ValueError as e:
            print(f"Erro: {e}")
            return
        self.repository.update_status_repo(id, new_status)
