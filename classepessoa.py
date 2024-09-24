class Pessoa:
    def __init__(self, matricula, nome, idade):
        self.Matricula = matricula
        self.Nome = nome
        self.Idade = idade

    def Mostrar(self):
        print(f'Matricula: {self.Matricula}\nNome: {self.Nome}\nIdade: {self.Idade}')

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, nota1,nota2,nota3):
        super().__init__(matricula, nome, idade)
        self.Notas = [nota1,nota2,nota3]
        self.Media = 0

    def Calcular_media(self):
        for i in self.Notas:
            self.Media += i
        self.Media /= len(self.Notas)
        print(f'Média do aluno: {self.Media}')

    def Estudar(self):
        print("Aluno está matriculado")

class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, carga_horaria, salario):
        super().__init__(matricula, nome, idade)
        self.Formacao = formacao
        self.Disciplina = disciplina
        self.Carga_Horaria = carga_horaria
        self.Salaria = salario

    def Lecionar(self):
        print(f"Professor {self.Nome} leciona {self.Disciplina}.")

aluno = Aluno(11909,"Lara",16,9,8,9)
aluno.Mostrar()
aluno.Calcular_media()
aluno.Estudar()

professor = Professor(1234,"Marcelo",30,"Filosofia","Filososfia",40,3333)
professor.Mostrar()
professor.Lecionar()
