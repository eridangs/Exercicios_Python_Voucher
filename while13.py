numero = input()
soma = 0

while True:
    while numero != "":
        soma = soma + int(numero[0])
        numero = numero[1:]
        
    print(soma)
    break