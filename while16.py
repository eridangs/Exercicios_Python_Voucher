c1 = 0
c2 = 0
c3 = 0
c4 =0
n = 0
b = 0
while True: 
    voto = int(input())
    if voto == 0:
        print(f'{c1} votos para candidato 1')
        print(f'{c2} votos para candidato 2')
        print(f'{c3} votos para candidato 3')
        print(f'{c4} votos para candidato 4')
        print(f'{n} votos nulos')
        print(f'{b} votos em branco')
        break
    elif voto == 1:
        c1 += 1
    elif voto == 2:
        c2 += 1
    elif voto == 3:
        c3 += 1
    elif voto == 4:
        c4 += 1
    elif voto == 5:
        n += 1
    elif voto == 6:
        b += 1
    else:
        print("valor invalido")