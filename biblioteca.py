class Biblioteca:
    def __init__(self) -> None:
        self.livros = []
    
    def AdicionarLivro(self,livro):
        self.livros.append(livro)
    
    def ConsultarDetalhe(self,titulo):
        livro = self.BuscarLivro(titulo)
        if livro:
            return livro
        else:
            print("Livro não encontrado")

    def BuscarLivro(self,titulo):
        for i in self.livros:
            if i.Titulo == titulo: #i.titulo necessario para acessar a string correspondente ao titulo, "instancia" o titulo ao i
                return i #retorna o livro com ambas as informações
    
    def EmprestarLivro(self,titulo):
        livro = self.BuscarLivro(titulo)
        if livro:
            if not livro.Emprestado:
                livro.Emprestado = True
                print("Emprestimo realizado.")
            else:
                print("Livro já está emprestado.")
        else:
            print("Livro não encontrado.")
        
    def ListarLivros(self):
        for i in self.livros:
            print(i)

