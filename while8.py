while True:
    a=float(input("Valor do produto 1: "))
    b=float(input("Valor do produto 2: "))
    c=float(input("Valor do produto 3: "))
    d=float(input("Valor do produto 4: "))
    e=float(input("Valor do produto 5: "))
    pagamento = int(input("Quantia usada para pagar: "))
    total = a + b + c + d + e
    print(f'Produto 1: R$ {a}')
    print(f'Produto 2: R${b}')
    print(f'Produto 3: R${c}')
    print(f'Produto 4: R${d}')
    print(f'Produto 5: R${e}')
    print(f'Total: R${total}')
    print(f'Dinheiro: R${pagamento}')
    troco = pagamento-total
    print(f'Troco: R${troco}')
    