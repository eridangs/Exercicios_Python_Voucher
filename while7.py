A = int(input("População de A: "))
B = int(input("População de B: "))
taxaA = float(input("Taxa de crescimento da população A em %: "))
taxaB = float(input("Taxa de crescimento da população B em %: "))
contador = 0
while A < B and taxaA > taxaB:
    crescA = A * (taxaA/100)
    A += crescA
    print(A)
    crescB = B * (taxaB/100)
    B += crescB
    print(B)
    contador += 1
    print(f'Levará {contador} anos para que a população A ultrapasse a população B.')