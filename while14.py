caderno= 0
caneta= 0
lapis= 0
borracha= 0
regua= 0
estoque = 0
saida = 0
while True:
        codigo = int(input("Digite o código do produto: "))
        print("Escolha a operação:")
        print("E-Entrada no estoque")
        print("S-Saída no estoque")
        print("R-Relatório")
        print("X-Sair")
        operacao = input("Digite a operação desejada: ")
        if operacao == "E":
            estoque = int(input("Quantidade a adicionar ao estoque do produto: "))
            if codigo == 10:
                caderno += estoque
            if codigo == 20:
                caneta += estoque
            if codigo == 30:
                lapis += estoque
            if codigo == 40:
                borracha += estoque
            if codigo == 50:
                regua += estoque
        elif operacao == "S":
            saida = int(input("Quantidade a retirar do estoque do produto: "))
            if codigo == 10:
                caderno -= saida
                if caderno < 0:
                    print("O estoque de caderno é menor que a quantidadade que se quer retirar do produto")
                    break
            if codigo == 20:
                caneta -= saida
                if caneta < 0:
                    print("O estoque de caneta é menor que a quantidadade que se quer retirar do produto")
                    break
            if codigo == 30:
                lapis -= saida
                if lapis < 0:
                    print("O estoque de lapis é menor que a quantidadade que se quer retirar do produto")
                    break
            if codigo == 40:
                borracha -= saida
                if borracha < 0:
                    print("O estoque de borracha é menor que a quantidadade que se quer retirar do produto")
                    break
            if codigo == 50:
                regua -= saida
                if regua < 0:
                    print("O estoque de regua é menor que a quantidadade que se quer retirar do produto")
                    break
        elif operacao == "R":
            print(f'Caderno tem {caderno} unidades no estoque')
            print(f'Caneta tem {caneta} unidades no estoque')
            print(f'Lápis tem {lapis} unidades no estoque')
            print(f'Borracha tem {borracha} unidades no estoque')
            print(f'Régua tem {regua} unidades no estoque')
        elif operacao == "X":
            break
        print(regua)
