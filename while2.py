while True:
    operacao = int(input("digite o número da operação desejada; 1_multiplicação, 2_divisão, 3_adição, 4_subtraçâ0 ou 5 para sair: "))
    if operacao == 1 or operacao == 2 or operacao == 3 or operacao == 4:
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        if operacao == 1:
              print(f'{a} x {b} = {a * b}')
        elif operacao == 2:
            if b == 0:
                 print("Não tem como dividir por zero")
            else:
                print(f'{a} / {b} = {a / b}')
        elif operacao == 3:
            print(f'{a} + {b} = {a + b}')
        elif operacao == 4:
            print(f'{a} - {b} = {a - b}')
    elif operacao == 5:
             print("Calculadora interrompida")
             print("Obrigada por utilizar nosso sistema")
             break