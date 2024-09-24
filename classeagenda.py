class Agenda():
    def __init__(self,dia,mes,ano):
        self.Dia = dia
        self.Mes = mes
        self.Ano = ano
        self.Anotacao = input("Anote na agenda: ")

    def ValidarData(self):
        ano_atual = 2024
        
        if self.Ano < ano_atual and  self > (ano_atual+100):
            print("Ano inválido.")
            self.ErroData()

        elif self.Mes > 12 or self.Mes <= 0:
            print("Mês inválido.")
            self.ErroData()

        elif self.Dia > 31 or self.Dia <= 0:
            print("Dia inválido.")
            self.ErroData()

    def ErroData(self):
        self.Dia = 0
        self.Mes = 0
        self.Ano = 0
        self.Anotacao = "***Data inválida***"

    def Mostrar(self):
        print(self.Dia,self.Mes,self.Ano,sep="/")
        print(f'________Nota________\n{self.Anotacao}')
        
Nota = Agenda(31,12,2025)
Nota.ValidarData()
Nota.Mostrar()
