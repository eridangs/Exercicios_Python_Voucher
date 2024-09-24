#Criar um sistema simples de agendamento de livros
#tem que ter uma classe livros e uma biblioteca
from biblioteca import Biblioteca
from livros import Livros

def ExibirMenu():
    print("1. Adicionar livro")
    print("2. Consultar detalhes do livro")
    print("3. Emprestar um livro")
    print("4. Devolver um livro")
    print("5. Listar todos os livros da biblioteca")
    print("6. Sair")

biblioteca = Biblioteca()
while True:
    ExibirMenu()
    op = int(input("Digite a opção: "))

    if op == 1:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o nome do autor: ")
        livro = Livros(titulo,autor)
        biblioteca.AdicionarLivro(livro)

    elif op == 2:
        titulo = input("Digite o título que quer buscar: ")
        detalhes = biblioteca.ConsultarDetalhe(titulo)
        print(detalhes)

    elif op == 3:
        titulo = input("Digite o título que quer buscar: ")
        biblioteca.EmprestarLivro(titulo)

    elif op == 4:
        titulo = input("Digite o título do livro que quer devolver: ")
        biblioteca.DevolverLivro(titulo)
    
    elif op == 5:
        biblioteca.ListarLivros()
    
    elif op == 6:
        break
