from models.exam import *
class ExamService:

    def __init__(self, repository):
        self.repository = repository

    def register_exam(self, name, sample_type):

        name = name.title()
        sample_type = sample_type.title()
        try:
            if not name.strip():
                raise ValueError("Nome do exame é obrigatório, não pode estar vazio!")
            if not sample_type.strip():
                raise ValueError("Tipo da amostra é obrigatório, não pode estar vazio!")
        except ValueError as e:
            print(f"Erro: {e}")
            return
        

        exam = Exam(name, sample_type)
        self.repository.register_exam_repo(exam)
        print("Exame cadastrado com sucesso!")

    def exam_exists(self, cpf):
        if self.repository.search_id_repo(cpf):
            return True
        else:
            return False
    
    def search_all(self):
        return self.repository.search_all_repo()

    def search_one_show(self, id):
        iden = self.repository.search_id_repo(id)
        if not iden:
            print("Nenhum exame cadastrado com esse código!")
        else:
            return print(dict(iden))
    
    def search_exam_id(self, id, callback):
        if self.repository.search_id_repo(id):
            
            return callback(self,id)
        
        else:
            print("Nenhum exame cadastrado com esse código!")

    def update_exam_name(self, id):

        name = Exam.update_exam_name(self)
        name.title()

        try:
            if not name.strip():
                raise ValueError("Nome do exame é obrigatório, não pode estar vazio!")
        except ValueError as e:
            print(f"Erro: {e}")
            return
        self.repository.update_name_repo(id, name)
        print("Nome do exame alterado com sucesso!")

    def update_exam_sample(self,id):

        sample = Exam.update_sample_type(self)
        sample.title()

        try: 
            if not sample.strip():
                raise ValueError("Tipo da amostra é obrigatório, não pode estar vazio!")
        except ValueError as e:
            print(f"Erro: {e}")
            return
        self.repository.update_sample_repo(id, sample)
        print("Tipo de amostra do exame alterado com sucesso!")
