class Circulo():
    def __init__(self,raio):
        self.Raio = raio
        self.pi = 3.14159

    def Mostrar(self):
        print(f'O raio equivale a {self.Raio}')
        self.Area()
        self.Comprimento()

    def Area(self):
        print(f'A área do círculo equivale a {self.pi*self.Raio**2}')

    def Comprimento(self):
        print(f'O comprimento do círculo equivale a {2*self.pi*self.Raio}')

circulo = Circulo(8)
circulo.Mostrar()