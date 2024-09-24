class Pessoa():
    nome = "Lara"
    idade = 16
    endereco = "Rua Espanha 694 Jardim Jacy"

    def metodos(self):
        print(f'{self.nome}')
        print(f'{self.idade}')
        print(f'{self.endereco}')

    def change_age(self):
        self.idade = int(input("Nova idade: "))

pessoa1 = Pessoa()
pessoa1.metodos()
pessoa1.change_age()
pessoa1.metodos()
