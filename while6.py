A = 80000
B = 200000
contador = 0
while A < B:
    crescA = A * 0.03
    A += crescA
    print(A)
    contador += 1
    print(f'Levará {contador} anos para que a população A ultrapasse a população B.')