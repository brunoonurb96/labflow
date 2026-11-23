from models.patient import Patient
from datetime import datetime
class PatientService:
    
    def __init__(self, repository):
        self.repository = repository

    def register_patient(self, cpf, name, birth, address, phone):

        try:
            if self.repository.search_cpf_repo(cpf):
                print("Paciente ja cadastrado!")
                return
            else:
                if not cpf.strip(): 
                    raise ValueError("CPF é obrigatório, não pode estar vazio!") 
                if not name.strip():
                    raise ValueError("Nome é obrigatório, não pode estar vazio!")
                if not birth.strip():
                    raise ValueError("Data de nascimento é obrigatório, não pode estar vazio!")
                try:
                    datetime.strptime(birth, "%Y-%m-%d")
                except ValueError:
                    raise ValueError("Data de nascimento tem que estar em formato AAAA-MM-DD") 
                if not address.strip():
                    raise ValueError("Endereço é obrigatório, não pode estar vazio!")
                if not phone.strip(): 
                    raise ValueError("Telefone é obrigatório, não pode estar vazio!")
                if not phone.isdigit():
                    raise ValueError("Digite apenas números em telefone!") 
        except ValueError as e:
            print(f"Erro: {e}")
            return
        name = name.title()
        patient = Patient(cpf, name, birth, address, phone)
        self.repository.register_patient_repo(patient)
    
    def search_one_show(self, cpf):
        patients = self.repository.search_cpf_repo(cpf)
        if not patients:
            print("Nenhum paciente cadastrado com esse CPF")
            return False
        else:
            for patient in patients:
                print(dict(patient))
            return True
    
    def search_all_serv(self):
        return self.repository.search_all()

    def search_cpf(self,cpf,callback):
        if self.repository.search_cpf_repo(cpf):
            
            return callback(self,cpf)

        else:
            print("Paciente não encontrado com esse CPF")

    def patient_exists(self, cpf):
        if self.repository.search_cpf_repo(cpf):
            return True
        else:
            return False
    
    def update_pat_name(self,cpf):
     
        name = Patient.update_patient_name(self)
        name = name.title()
        try:
            if not name.strip():
                raise ValueError("Nome é obrigatório, não pode estar vazio!")
            
        except ValueError as e:
            print(f"Erro: ", e)
            return
                
        self.repository.update_name_repo(cpf,name)


    def update_pat_birth(self,cpf):

        
        birth = Patient.update_birth(self)
        try: 
            if not birth.strip():
                raise ValueError("Data de nascimento é obrigatório, não pode estar vazio!")
            try:
                datetime.strptime(birth, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Data de nascimento tem que estar em formato AAAA-MM-DD") 

        except ValueError as e:
            print(f"Erro: {e}")
            return
        self.repository.update_birth_repo(cpf,birth)

    def update_pat_address(self, cpf):

        address = Patient.update_address(self)
        try:
            if not address.strip():
                raise ValueError("Endereço é obrigatório, não pode estar vazio!")
        except ValueError as e:
            print(f"Erro: {e}")
            return
        self.repository.update_address_repo(cpf,address)

    def update_pat_phone(self,cpf):

        phone = Patient.update_phone(self)
        try:
            if not phone.strip(): 
                raise ValueError("Telefone é obrigatório, não pode estar vazio!")
            if not phone.isdigit():
                raise ValueError("Digite apenas números em telefone!") 
        except ValueError as e:
            print(f"Erro: {e}")
            return
        self.repository.update_phone_repo(cpf,phone)