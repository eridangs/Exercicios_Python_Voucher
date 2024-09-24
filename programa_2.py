import random

class Cartela_Bingo:
    def __init__(self):
        self.ColunaB = []
        self.ColunaI = []
        self.ColunaN = []
        self.ColunaG = []
        self.ColunaO = []
        
    def Adicionar_à_Lista(self):
        while len(self.ColunaB) != 5:
            b = random.randint(1,15)
            if  not b in self.ColunaB:
                self.ColunaB.append(b)
        
        while len(self.ColunaI) != 5:
            i = random.randint(16,30)
            if not i in self.ColunaI:
                self.ColunaI.append(i)

        while len(self.ColunaN) != 5:
            n = random.randint(31,45)
            if not n in self.ColunaN:
                self.ColunaN.append(n) 
        self.ColunaN[2] = "#"  

        while len(self.ColunaG) != 5:
            g = random.randint(46,60)
            if not g in self.ColunaG:
                self.ColunaG.append(g)

        while len(self.ColunaO) != 5:
            o = random.randint(61,75)
            if not o in self.ColunaO:
                self.ColunaO.append(o)


    def Mostrar(self):
      
        print("_____BEM VINDO AO BINGO_____\nEssa é a sua cartela: ")
        print(    "  ","B  I  N  G  O")
        print("L1", self.ColunaB[0],self.ColunaI[0],self.ColunaN[0],self.ColunaG[0],self.ColunaO[0])
        print("L2", self.ColunaB[1],self.ColunaI[1],self.ColunaN[1],self.ColunaG[1],self.ColunaO[1])
        print("L3", self.ColunaB[2],self.ColunaI[2],self.ColunaN[2],self.ColunaG[2],self.ColunaO[2])
        print("L4", self.ColunaB[3],self.ColunaI[3],self.ColunaN[3],self.ColunaG[3],self.ColunaO[3])
        print("L5", self.ColunaB[4],self.ColunaI[4],self.ColunaN[4],self.ColunaG[4],self.ColunaO[4])

    def Inserir_numero(self):
        self.Numero = int(input("Qual número foi sorteado? "))
        if self.Numero <= 15:
            if self.Numero in self.ColunaB:
                for i  in range(len(self.ColunaB)):
                    if self.ColunaB[i] == self.Numero:
                        self.ColunaB[i] = "#"

        if self.Numero >= 16 and self.Numero <= 30:
            if self.Numero in self.ColunaI:
                for i in range(len(self.ColunaI)):
                    if self.ColunaI[i] == self.Numero:
                        self.ColunaI[i] = "#"

        if self.Numero >= 31 and self.Numero <= 45:
            if self.Numero in self.ColunaN:
                for i in range(len(self.ColunaN)):
                    if self.ColunaN[i] == self.Numero:
                        self.ColunaN[i] = "#"

        if self.Numero >= 46 and self.Numero <= 60:
            if self.Numero in self.ColunaG:
                for i in range(len(self.ColunaG)):
                    if self.ColunaG[i] == self.Numero:
                        self.ColunaG[i] = "#"

        if self.Numero >= 61 and self.Numero <= 75:
            if self.Numero in self.ColunaO:
                for i in range(len(self.ColunaO)):
                    if self.ColunaO[i] == self.Numero:
                        self.ColunaO[i] = "#"

    def Validar_Bingo_Coluna(self):
        if self.ColunaB[0] == "#" and self.ColunaB[1] == "#" and self.ColunaB[2] == "#" and  self.ColunaB[3] == "#" and self.ColunaB[4] == "#":
            print("Você fez BINGO na coluna B!")
        if self.ColunaI[0] == "#" and self.ColunaI[1] == "#" and self.ColunaI[2] == "#" and  self.ColunaI[3] == "#" and self.ColunaI[4] == "#":
            print("Você fez BINGO na coluna I!")
        if self.ColunaN[0] == "#" and self.ColunaN[1] == "#" and self.ColunaN[2] == "#" and  self.ColunaN[3] == "#" and self.ColunaN[4] == "#":
            print("Você fez BINGO na coluna N!")
        if self.ColunaG[0] == "#" and self.ColunaG[1] == "#" and self.ColunaG[2] == "#" and  self.ColunaG[3] == "#" and self.ColunaG[4] == "#":
            print("Você fez BINGO na coluna G!")
        if self.ColunaO[0] == "#" and self.ColunaO[1] == "#" and self.ColunaO[2] == "#" and  self.ColunaO[3] == "#" and self.ColunaO[4] == "#":
            print("Você fez BINGO na coluna O!")

    def Validar_Bingo_Linha(self):
        if self.ColunaB[0] == "#" and self.ColunaI[0] == "#" and self.ColunaN[0] == "#" and self.ColunaG[0] == "#" and self.ColunaO[0] == "#":
            print("Você fez Bingo na L1!")
        if self.ColunaB[1] == "#" and self.ColunaI[1] == "#" and self.ColunaN[1] == "#" and self.ColunaG[1] == "#" and self.ColunaO[1] == "#":
            print("Você fez Bingo na L2!")
        if self.ColunaB[2] == "#" and self.ColunaI[2] == "#" and self.ColunaN[2] == "#" and self.ColunaG[2] == "#" and self.ColunaO[2] == "#":
            print("Você fez Bingo na linha L3!")
        if self.ColunaB[3] == "#" and self.ColunaI[3] == "#" and self.ColunaN[3] == "#" and self.ColunaG[3] == "#" and self.ColunaO[3] == "#":
            print("Você fez Bingo na linha L4!")
        if self.ColunaB[4] == "#" and self.ColunaI[4] == "#" and self.ColunaN[4] == "#" and self.ColunaG[4] == "#" and self.ColunaO[4] == "#":
            print("Você fez Bingo na Linha L5!")

    def Validar_Bingo_Diagonal(self):
        if self.ColunaB[0] == "#" and self.ColunaI[1] == "#" and self.ColunaN[2] == "#" and self.ColunaG[3] == "#" and self.ColunaO[4] == "#":
            print("Você fez 1 Bingo na diagonal!")
        if self.ColunaB[4] == "#" and self.ColunaI[3] == "#" and self.ColunaN[2] == "#" and self.ColunaG[1] == "#" and self.ColunaO[0] == "#":
            print("Você fez 1 Bingo na diagonal!")
        
        
cartela1 = Cartela_Bingo()
cartela1.Adicionar_à_Lista()
while True:
    cartela1.Mostrar()
    cartela1.Validar_Bingo_Coluna()
    cartela1.Validar_Bingo_Linha()
    cartela1.Validar_Bingo_Diagonal()
    cartela1.Inserir_numero()