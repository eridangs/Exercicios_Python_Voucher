class Aluno():
    def __init__(self,nome,matricula,nota1,nota2,nota3,nota4):
        self.Nome = nome 
        self.RA = matricula
        self.Notas = [nota1,nota2,nota3,nota4]
        self.Situacao = 0

    def Media(self):
        for i in self.Notas:
            self.Situacao += i
        self.Situacao /= len(self.Notas)
        if self.Situacao >= 7:
            self.Situacao = "Aprovado"
        elif self.Situacao >= 5 and self.Situacao <= 6.9:
            self.Situacao = "Exame"
        elif self.Situacao < 5:
            self.Situacao = "Reprovado"
        
    def Mostrar(self):
        print(f'{self.Nome}\n{self.RA}\n{self.Situacao}')
    
aluno1 = Aluno("Lara","119045",8,9,10,9)
aluno1.Media()
aluno1.Mostrar()