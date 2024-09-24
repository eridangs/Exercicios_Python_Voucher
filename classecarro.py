class Carro():
    def __init__(self,modelo,marca,cor,ano,valor,consumo):
        self.Modelo = modelo
        self.Marca = marca
        self.Cor = cor
        self.Ano = ano
        self.Valor = valor
        self.Consumo = consumo
        self.Nivel = 0
    
    def Abastecer(self):
        self.Gasolina = int(input("Litros abastecidos: "))
    
    def Kilometragem(self):
        self.Abastecer()
        self.Distancia_percorrida = int(input("Distância em km percorrida: "))
        self.Nivel = self.Distancia_percorrida / self.Consumo
        print(f'Foram abastecidos {self.Gasolina} litros de gasolina e percorridos {self.Distancia_percorrida} Kms.\nForam gastos {self.Nivel}l por {self.Distancia_percorrida} Km. ')

    def IPVA(self):
        self.Imposto = self.Valor*0.025
        print(f'O IPVA do carro custa {self.Imposto}')
    
carro1 = Carro("SUV","Peugeot","Vermelho",2017,104990,11.2)
carro1.Kilometragem()
carro1.IPVA

