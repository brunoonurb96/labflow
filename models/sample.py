class Sample:

    def __init__(self, cpf, exam, date):
        self.cpf = cpf
        self.exam = exam
        self.date = date
        self.status = ""

    def update_samp_cpf(self):
        new_cpf = input("Digite um novo CPF para essa amostra: ")
        self.cpf = new_cpf
        return self.cpf
    
    def update_samp_exam(self):
        new_exam = input("Digite um novo código de exame para essa amostra: ")
        self.exam = new_exam
        return self.exam

    def update_samp_date(self):
        new_date = input("Digite uma nova data em que foi coletado a amostra: ")
        self.date = new_date
        return self.date

    def update_samp_status(self):
        new_status = input("Digite um novo status para essa amostra: ")
        self.status = new_status
        return self.status

    