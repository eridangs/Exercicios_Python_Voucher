v= float(input("Valor do produto: "))
P= input("Forma de pagamento: dinheiro, pix, crédito, duasX ou trêsX: ")
if P == "dinheiro" or "pix":
   print(f'O valor do produto a vista no dinheiro ou pix é R${(v - (v*0.1))}')
if P=="crédito":
    print(f'O valor do produto a vista no cartão de crédito é R$ {(v - (v*0.05))}')
if P == "duasX":
    print(f'O valor de cada uma das 2 parcelas custa R$ {(v/2)}')
if P == "trêsX":
    print(f'Cada uma das 3 parcelas custa R$ {(v+(v*0.1))/(3)}')
else:
    print("Forma de pagamento não identificada")