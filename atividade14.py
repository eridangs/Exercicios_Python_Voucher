saida1 = (input("Digite o código do produto: "))
saida2 = (input("Digite o código do produto: "))
soma=0
if saida1 == "100" or "101" or "102" or "103" or "201" or "202" or "203" or saida2 == "100" or "101" or "102" or "103" or "201" or "202" or "203":
    if saida1 == "100" or saida2 == "100":
        soma+=11.20
    if saida1 == "101" or saida2 == "101":
        soma+=8.30
    if saida1 == "102" or saida2 == "102":
        soma+=11.50
    if saida1 == "103" or saida2 == "103":
        soma+=16.20
    if saida1 == "201" or saida2 == "201":
        soma+=6
    if saida1 == "202" or saida2 == "202":
        soma+=7.50
    if saida1 == "203" or saida2 == "203":
        soma+=4.70
    print(soma)
else:
    print("Código invalido")