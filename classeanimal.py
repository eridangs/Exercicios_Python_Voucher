class Animal:
    def __init__(self,nome,cor):
        self.Nome = nome
        self.Cor = cor

class Cachorro(Animal):
    def __init__(self, nome, cor,peso):
        super().__init__(nome,cor)
        self.peso = peso
    
    def MostrarNome(self):
        print(f'Olá meu nome é {self.Nome}')

class Gato(Animal):
    def __init__(self, nome, cor,peso):
        super().__init__(nome, cor)
        self.peso = peso
    
    def MostrarNome(self):
        print(f'Olá meu nome é {self.Nome}')

dog = Cachorro("Jake","Preto",12)
dog.MostrarNome()
cat = Gato("Kate","Carijo",4)
cat.MostrarNome()