#Sorteio de números
import random

class Sorteio:
    def Roleta(self):
        self.lista = []
        while len(self.lista) < 75:
            self.Numero_sorteado = random.randrange(1,76)
            if  not self.Numero_sorteado in self.lista:
                self.lista.append(self.Numero_sorteado)
            
    def Show(self):
        self.Roleta()
        for Numero_sorteado in self.lista:
            if Numero_sorteado >= 1 and Numero_sorteado <= 15:
                print(f'Na coluna B: {Numero_sorteado}.')
            elif Numero_sorteado >= 16 and Numero_sorteado <= 30:
                print(f'Na coluna I: {Numero_sorteado}.')
            elif Numero_sorteado >= 31 and Numero_sorteado <= 45:
                print(f'Na coluna N: {Numero_sorteado}.')
            elif Numero_sorteado >= 46 and Numero_sorteado <= 60:
                print(f'Na coluna G: {Numero_sorteado}.')
            else:
                print(f'Na coluna O: {Numero_sorteado}.')
        print(f"Todos os 75 números foram sorteados nessa ordem: {self.lista}.")

rodada1 = Sorteio()
while True:
    print("Para rodar o Bingo - 1")
    print("Para parar - 2")
    op = int(input("Sua escolha: "))
    if op == 1:
        rodada1.Show()
    elif op == 2:
        print("Obrigado por participar desse bingo!")
        break