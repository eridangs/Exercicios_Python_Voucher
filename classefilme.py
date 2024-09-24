class Filme():
    def __init__(self,nome,duracao):
        self.Nome = nome
        self.Duracao = duracao

    def Metodo(self):
        self.Play = "Foi dado play no filme"
        print(self.Nome)
        print(self.Duracao)
        print(self.Play)

class Acao(Filme):
    def __init__(self, nome, duracao, explodir):
        super().__init__(nome,duracao)
        self.Acao_ = explodir

    def Movimento(self):
        print(self.Acao_)

class Drama(Filme):
    def __init__(self, nome, duracao, chorar):
        super().__init__(nome, duracao)
        self.Chorar = chorar

    def Movimento(self):
        print(self.Chorar)

class Suspense(Filme):
    def __init__(self, nome, duracao, assustar):
        super().__init__(nome, duracao)
        self.Assustar = assustar

    def Movimento(self):
        print(self.Assustar)
        

filme1 = Acao("Duna: Parte 2", "160 minutos","Explosão!!!")
filme1.Metodo()
filme1.Movimento()
filme2 = Drama("Veronica", "90 minutos", "Cai em prantos!")
filme2.Metodo()
filme2.Movimento()
filme3 = Suspense("O cavalheiro das trevas","150 minutos", "Susto!!!")
filme3.Metodo()
filme3.Movimento()
  