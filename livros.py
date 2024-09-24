class Livros:
    def __init__(self,titulo,autor):
        self.Titulo = titulo
        self.Autor = autor
        self.Emprestado = False
    
    def __str__(self):
        status ='Disponivel'
        if self.Emprestado == True:
            status = 'Emprestado'
        return f"{self.Titulo, self.Autor} - {status}"