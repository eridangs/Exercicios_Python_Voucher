class Livro():
    def __init__(self,nome,autor,editora,paginas):
        self.Nome = nome
        self.Autor = autor
        self.Editora = editora
        self.Paginas = paginas

    def Showdetails(self):
        print(f'{self.Nome}\n{self.Autor}\n{self.Editora}\n{self.Paginas}')

    def ChangeEditora(self):
        self.Editora = input("Mudar editora: ")

livro1 = Livro("Tudo bem não estar tudo bem","Megan Divine","estante",197)
livro1.ChangeEditora()
livro1.Showdetails()