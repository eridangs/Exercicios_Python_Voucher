class Triangulo():
    def __init__(self):
        self.LadoA = int(input("Informe o lado A do triângulo: "))
        self.LadoB = int(input("Informe o lado B do triângulo: "))
        self.LadoC = int(input("Informe o lado C do triângulo: "))

    def Perimetro(self):
        print(f'O perímetro desde triângulo é {self.LadoA + self.LadoB + self.LadoC}')

    def Maior_Lado(self):
        Maior = self.LadoA
        if self.LadoB > Maior:
            Maior = self.LadoB
        if self.LadoC > Maior:
            Maior = self.LadoC
        print("O maior lado é",Maior)

triangulo1 = Triangulo()
triangulo1.Perimetro()
triangulo1.Maior_Lado()
