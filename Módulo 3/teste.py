class Person:
    def __init__(self, nome):
        self.nome = nome
    
    def saudacao(self):
        print("Olá, meu nome é", self.nome)

person = Person("Amanda")
person.saudacao()
