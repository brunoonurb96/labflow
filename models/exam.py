class Exam:

    def __init__(self, name, sample_type):
        self.name = name
        self.sample = sample_type



    def update_exam_name(self):
        new_name = input("Digite um novo nome para esse exame: ")
        self.name = new_name
        return self.name

    def update_sample_type(self):
        new_sample = input("Digite um novo tipo de amostra desse exame: ")
        self.sample = new_sample
        return self.sample