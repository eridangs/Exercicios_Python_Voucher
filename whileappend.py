carrinhocompras= []
while True:
    print("MENU:", "\n", "Digite 1 para visualizar o carrinho de compra:", "\n", "Digite 2 para selecionar produtos:", "\n" " Digite 3 para sair")
    op = int(input("Digite a opção do menu: "))
    if op == 3:
        break
    if op == 1:
        print(f'Produtos do carrinho: {carrinhocompras}')
    if op == 2:
        print("Selecione o codigo dos produtos:", "\n", "Digite 1 para adicionar HEADSET:", "\n", "Digite 2 para adicionar MOUSE:", "\n" " Digite 3 para adicionar TECLADO")
        cod = int(input("Digite o codigo: "))
        if cod == 1:
            carrinhocompras.append("HEADSET")
        elif cod == 2:
            carrinhocompras.append("MOUSE")
        elif cod  == 3:
            carrinhocompras.append("TECLADO")