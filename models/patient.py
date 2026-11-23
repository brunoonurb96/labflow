class Patient:

    def __init__(self, cpf, name, birth, address, phone):
        self.cpf = cpf
        self.name = name
        self.birth = birth
        self.address = address
        self.phone = phone

    def update_patient_name(self):
        new_name = input("Digite um nome para esse paciente: ")
        self.name = new_name
        return self.name

    def update_birth(self):
        new_birth = input("Digite uma data de nascimento para esse paciente (formato AAAA-MM-DD): ")
        self.birth = new_birth
        return self.birth

    def update_address(self):
        new_address = input("Digite um endereço para esse paciente: ")
        self.address = new_address
        return self.address

    def update_phone(self):
        new_phone = input("Digite um telefone para esse paciente: ")
        self.phone = new_phone
        return self.phone