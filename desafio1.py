ALIMENTOS=["LEITE","FEIJÃO","CENOURA","BANANA"]
Valimentos = [6,9,8,5]
HIGIENE=['PAPEL HIGIENICO',"SABONETE","DETERGENTE","ESPONJA"]
Vhigiene= [12, 3, 4, 2]
PRODUTOS_P_CASA=["LENÇOL","CABIDE","PORTA LOUÇAS","PILHA"]
Vprodutospcasa=[40, 15, 50, 20]
carrinhocompras = []
totalcarrinho = 0
valores_ordenados = []
lista = []
print("Faça login para adicionar produtos ao carrinho!","\n","Informe o tipo de usuário que voçê é: ")
usuario = input("FUNCIONÁRIO OU CLIENTE: ")
if usuario == "cliente" or usuario =='Cliente' or usuario=='CLIENTE':  #USUÁRIO
    print("Informe seu nome e CPF:")
    nome = input('Nome: ')
    CPF = input('CPF: ')
    while usuario== "cliente" or usuario == "Cliente" or usuario== "CLIENTE" :
        print("Seja bem vindo ao mercado.","\n", "Explore as opções das seções abaixo ao selecionar o número  correspondente:","\n","1_ALIMENTOS, 2_HIGIENE, 3_PRODUTOS PARA CASA, 4_SAIR DO MERCADO, 5_FINALIZAR COMPRA.")
        secao = int(input(""))
        if secao == 1:  #CATEGORIA 1
            print(f'Produtos alimenticios: {ALIMENTOS}')
            print(f'Digite o numero 1 para adicionar {ALIMENTOS[0]} ao carrinho, 2 para adicionar {ALIMENTOS[1]}, 3 para adicionar {ALIMENTOS[2]} e 4 para adicinar {ALIMENTOS[3]}:')
            escolha = int(input("Produto escolhido: ")) #demonstração apenas com alimentos[0]
            if escolha == 1:  #ADICIONA PRODUTO AO CARRINHO
                a = input(f'Deseja adicionar {ALIMENTOS[0]} ao carrinho? ')
                if a == "Sim" or a == "sim" or a == "SIM":
                    carrinhocompras.append([ALIMENTOS[0]])
                    totalcarrinho += Valimentos[0]
                    valores_ordenados.append([Valimentos[0]])
                    print(ALIMENTOS[0],"foi adicionado ao carrinho, seu carrinho agora tem",(carrinhocompras)) 
                    confirmacao= int(input("Digite 1 para voltar ao início e visualizar opções ou 2 para retirar produto do carrinho: "))
                    if confirmacao == 1:
                        totalcarrinho = totalcarrinho
                    elif confirmacao == 2:  #EXCLUI PRODUTO DO CARRINHO
                        retirado = carrinhocompras.pop() 
                        remove = valores_ordenados.pop()
                        totalcarrinho -= Vprodutospcasa[0]
                        print(f'{retirado} foi retirado do seu carrinho.')
                        print(f'Seu carrinho agora tem : {carrinhocompras}')
        if secao == 2:  #CATEGORIA 2
            print(f'Produtos higienicos: {HIGIENE}')
            print(f'Digite o numero 1 para adicionar {HIGIENE[0]} ao carrinho, 2 para adicionar {HIGIENE[1]}, 3 para adicionar {HIGIENE[2]} e 4 para adicinar {HIGIENE[3]}:')
            escolha = int(input("Produto escolhido: ")) #demonstração apenas com higiene[0]
            if escolha == 1:  #ADICIONA PRODUTO AO CARRINHO
                a = input(f'Deseja adicionar {HIGIENE[0]} ao carrinho? ')
                if a == "Sim" or a == "sim" or a == "SIM":
                    carrinhocompras.append([HIGIENE[0]])
                    totalcarrinho += Vhigiene[0]
                    valores_ordenados.append([Vhigiene[0]])
                    print(HIGIENE[0],"foi adicionado ao carrinho, seu carrinho agora tem",(carrinhocompras))
                    confirmacao= int(input("Digite 1 para voltar ao início e visualizar opções ou 2 para retirar produto do carrinho: "))
                    if confirmacao == 1:
                        totalcarrinho = totalcarrinho
                    elif confirmacao == 2:  #EXCLUI PRODUTO DO CARRINHO
                        retirado = carrinhocompras.pop() #como retirar o valor repetido
                        remove = valores_ordenados.pop()
                        totalcarrinho -= Vhigiene[0]
                        print(f'{retirado} foi retirado do seu carrinho.')
                        print(f'Seu carrinho agora tem : {carrinhocompras}')
        if secao == 3:  #CATEGORIA 3
            print(f'Produtos para casa: {PRODUTOS_P_CASA}')
            print(f'Digite o numero 1 para adicionar {PRODUTOS_P_CASA[0]} ao carrinho, 2 para adicionar {PRODUTOS_P_CASA[1]}, 3 para adicionar {PRODUTOS_P_CASA[2]} e 4 para adicinar {PRODUTOS_P_CASA[3]}:')
            escolha = int(input("Produto escolhido: ")) #demonstração apenas com produtos_p_casa[0]
            if escolha == 1:  #ADICIONA PRODUTO AO CARRINHO
                a = input(f'Deseja adicionar {PRODUTOS_P_CASA[0]} ao carrinho? ')
                if a == "Sim" or a == "sim" or a == "SIM":
                    carrinhocompras.append([PRODUTOS_P_CASA[0]])
                    totalcarrinho += Vprodutospcasa[0]
                    valores_ordenados.append([Vprodutospcasa[0]])
                    print(PRODUTOS_P_CASA[0],"foi adicionado ao carrinho, seu carrinho agora tem",(carrinhocompras))
                    confirmacao= int(input("Digite 1 para voltar ao início e visualizar opções ou 2 para retirar produto do carrinho: "))
                    if confirmacao == 1:
                        totalcarrinho = totalcarrinho
                    elif confirmacao == 2:  #EXCLUI PRODUTO DO CARRINHO
                        retirado = carrinhocompras.pop()
                        remove = valores_ordenados.pop()
                        totalcarrinho -= Vprodutospcasa[0]
                        print(f'{retirado} foi retirado do seu carrinho.')
                        print(f'Seu carrinho agora tem : {carrinhocompras}')
        if secao == 4:  #SAIR
            print("Volte sempre.")
            exit()
        if secao == 5:  #FINALIZAR COMPRA
           if carrinhocompras == []:
               print("Não há produtos no carrinho para finalizar a compra.")
           else:
                nacional = totalcarrinho*0.05
                estadual = totalcarrinho*0.08
                municipal = totalcarrinho*0.12
                totalcarrinho += nacional+estadual+municipal
                print(f'Total dos produtos + impostos: R${totalcarrinho}')
                print(f'Produtos dentro do carrinho {carrinhocompras}')
                print(f'Valor do produto {valores_ordenados} em ordem de adição')
                while True:    
                    pagamento= int(input("Digite o número correspondente a forma de pagamento 1-dinheiro, 2-pix ou 3-cartão): "))
                    if pagamento == 1:  #DINHEIRO
                        valor=int(input("Valor disponível para pagamento: "))
                        if valor >= totalcarrinho:
                            troco = (valor-totalcarrinho)
                            print(f'Seu troco é R$ {troco}.')
                            print(f'Obrigado por comprar conosco, {nome}!')
                            print('---'*20)
                            print("Nota fiscal da sua compra")  #NOTA FISCAL
                            print(f'Cliente: {nome}\nCPF: {CPF}')
                            for n,carrinhocompras in zip(valores_ordenados,carrinhocompras):
                                print(f'Produto: {carrinhocompras}={n}')
                            print(f'Imposto nacional 5%: {nacional}\nImposto estadual 8%: {estadual}\nImposto municipal 12%: {municipal}')
                            print(f'Valor sem impostos: {totalcarrinho-nacional-estadual-municipal}\nValor final com impostos pagos: {totalcarrinho}')
                            exit()
                        else:
                            print("Valor insuficiente, selecione outra forma de pagamento.")
                    elif pagamento == 2:  #PIX
                        valor=int(input("Digite o saldo existente em sua conta: "))
                        if valor >= totalcarrinho:
                            print(f'Sua compra foi aprovada.')
                            print(f'Obrigado por comprar conosco, {nome}!')
                            print('---'*20)
                            print("Nota fiscal da sua compra")  #NOTA FISCAL
                            print(f'Cliente: {nome}\nCPF: {CPF}')
                            for n,carrinhocompras in zip(valores_ordenados,carrinhocompras):
                                print(f'Produto: {carrinhocompras}={n}')
                            print(f'Imposto nacional 5%: {nacional}\nImposto estadual 8%: {estadual}\nImposto municipal 12%: {municipal}')
                            print(f'Valor sem impostos: {totalcarrinho-nacional-estadual-municipal}\nValor final com impostos pagos: {totalcarrinho}')
                            exit()
                        else:
                            print("Valor insuficiente, selecione outra forma de pagamento.")
                    elif pagamento == 3:  #CARTÃO
                        b= int(input("Digite 1 para pagar com cartão de débito e 2 para pagar com cartão de crédito: "))
                        if b == 1 or b == 2:
                            valor=int(input("Digite o saldo existente em sua conta: "))
                            if valor >= totalcarrinho:
                                print(f'Sua compra foi aprovada.')
                                print(f'Obrigado por comprar conosco, {nome}!')
                                print('---'*20)
                                print("Nota fiscal da sua compra")  #NOTA FISCAL
                                print(f'Cliente: {nome}\nCPF: {CPF}')
                                for n,carrinhocompras in zip(valores_ordenados,carrinhocompras):
                                    print(f'Produto: {carrinhocompras}={n}')
                                print(f'Imposto nacional 5%: {nacional}\nImposto estadual 8%: {estadual}\nImposto municipal 12%: {municipal}')
                                print(f'Valor sem impostos: {totalcarrinho-nacional-estadual-municipal}\nValor final com impostos pagos: {totalcarrinho}')
                                exit()
                        else:
                            print("Valor insuficiente, selecione outra forma de pagamento.")

elif usuario == "Funcionário" or usuario == "funcionário" or usuario == "FUNCIONÁRIO" or usuario == "Funcionario" or usuario == "funcionario" or usuario == "FUNCIONARIO":  #FUNCIONÁRIO
    print("Informe sua matrícula, seu nome, sua data de nascimento e seu CPF.")
    matricula = float(input("Matrícula: "))
    nome = input("Nome: ")
    cpf = input("CPF: ")
    dateofbirth = input("Data de nascimento no formato dd/mm/aaaa: ")
    leite = ["Alimento","Leite","3","6"]
    papelhigienico = ["Higiene","Papel higienico","6","12"]
    lencol = ["Produtos para casa","Lençol","9","40"]
    novoproduto = []
    while usuario == "Funcionário" or usuario == "funcionário" or usuario == "FUNCIONÁRIO" or usuario == "Funcionario" or usuario == "funcionario" or usuario == "FUNCIONARIO":
        print(f'Olá {nome}!')
        funcao = int(input("Qual função deseja executar?\nDigite 1 para consultar o estoque, 2 para atualizar o estoque, 3 para adicionar um novo produto 4 para mudar o preço de um produto ou 5 para sair: "))
        if funcao == 1:  #CONSULTAR ESTOQUE
            if novoproduto != []:
               print(f'Leite tem {leite[2]} unidades\nPapel higienico tem {papelhigienico[2]} unidades\nLençol tem {lencol[2]} unidades\n{novoproduto[1]} tem {novoproduto[2]} unidades.') 
            else:
                print(f'Leite tem {leite[2]} unidades\nPapel higienico tem {papelhigienico[2]} unidades\nLençol tem {lencol[2]} unidades.')
        elif funcao == 2:  #ATUALIZAR ESTOQUE
            print(f'O estoque de qual produto deseja atualizar?')
            if novoproduto != []:
                opc= int(input(f'Digite 1 para atualizar o estoque de {leite[1]}, 2 para atualizar o estoque de {papelhigienico[1]}, 3 para atualizar o estoque de {lencol[1]}, 4 para atualizar o estoque de {novoproduto[1]}: '))
                if opc == 1:
                    novo = input(f'Nova quantidade de {leite[1]}: ')
                    leite[2]= novo
                    print("Estoque atualizado!")
                elif opc == 2:
                    novo = input(f'Nova quantidade de {papelhigienico[1]}: ')
                    papelhigienico[2]= novo
                    print("Estoque atualizado!")
                elif opc == 3:
                    novo = input(f'Nova quantidade de {lencol[1]}: ')
                    lencol[2]= novo
                    print("Estoque atualizado!")
                elif opc == 4:
                    novo = input(f'Nova quantidade de {novoproduto[1]}: ')
                    novoproduto[2]= novo
                    print("Estoque atualizado!")
            else:
                opc= int(input(f'Digite 1 para atualizar o estoque de {leite[1]}, 2 para atualizar o estoque de {papelhigienico[1]}, 3 para atualizar o estoque de {lencol[1]}: '))
                if opc == 1:
                    novo = input(f'Nova quantidade de {leite[1]}: ')
                    leite[2]= novo
                    print("Estoque atualizado!")
                elif opc == 2:
                    novo = input(f'Nova quantidade de {papelhigienico[1]}: ')
                    papelhigienico[2]= novo
                    print("Estoque atualizado!")
                elif opc == 3:
                    novo = input(f'Nova quantidade de {lencol[1]}: ')
                    lencol[2]= novo
                    print("Estoque atualizado!")
        elif funcao == 3: #ADICIONAR PRODUTO
            tipo = int(input("Selecione a categoria do produto, 1 para Alimentos, 2 para Higiênicos ou 3 para Produtos para casa: "))
            if tipo == 1:
                nomeproduto = input("Nome do produto: ")
                ALIMENTOS.append(nomeproduto)
                codigoproduto = input("Código do produto: ")
                precoproduto = int(input("Preço do produto: "))
                Valimentos.append(precoproduto)
                estoque = input("Quantidade estocada: ")
                novoproduto = ["Alimentos",nomeproduto,estoque,precoproduto,codigoproduto]
                print(f'{nomeproduto} foi adicionado à Alimentos, que agora tem: {ALIMENTOS}.')
            elif tipo == 2:
                nomeproduto = input("Nome do produto: ")
                HIGIENE.append(nomeproduto)
                codigoproduto = input("Código do produto: ")
                precoproduto = int(input("Preço do produto: "))
                Vhigiene.append(precoproduto)
                estoque = input("Quantidade estocada: ")                
                novoproduto= ["HIGIENE",nomeproduto,estoque,precoproduto,codigoproduto]
                print(f'{nomeproduto} foi adicionado à Higiênicos, que agora tem: {HIGIENE}.')
            elif tipo == 3:
                nomeproduto = input("Nome do produto: ")
                PRODUTOS_P_CASA.append(nomeproduto)
                codigoproduto = input("Código do produto: ")
                precoproduto = int(input("Preço do produto: "))
                Vprodutospcasa.append(precoproduto)
                estoque = input("Quantidade estocada: ")
                novoproduto = ["Produtos para casa",nomeproduto,estoque,precoproduto,codigoproduto]
                print(f'{nomeproduto} foi adicionado à Produtos para casa, que agora tem: {PRODUTOS_P_CASA}.')
            print(f'Informações do produto adicionado:\nCategoria: {novoproduto[0]}\nNome: {novoproduto[1]}\nQuantidade disponível: {novoproduto[2]}\nPreço: {novoproduto[3]}\nCodigo cadastrado: {novoproduto[4]}')
        elif funcao == 4: #MUDAR O PREÇO
            c= input("Deseja alterar o preço de algum produto? Sim ou Não? ")
            if c == "Sim" or c == "sim" or c == "SIM":
                if novoproduto != []:
                    mudanca = int(input(f'Digite 1 para alterar o preço de {leite[1]}, 2 para alterar o preço de {papelhigienico[1]}, 3 para alterar o preço de {lencol[1]} ou 4 para alterar o preço de {novoproduto[1]}: '))
                    if mudanca == 1:
                        novopreco = input("Digite o novo preço de ",leite[1],": ")
                        leite[3] = novopreco
                        print("Preço atualizado!")
                    if mudanca == 2:
                        novopreco = input(f'Digite o novo preço de {papelhigienico[1]}: ')
                        papelhigienico[3] = novopreco
                        print("Preço atualizado!")
                    if mudanca == 3:
                        novopreco = input(f'Digite o novo preço de {lencol[1]}: ')
                        lencol[3] = novopreco
                        print("Preço atualizado!")
                    if mudanca == 4:
                        novopreco = input(f'Digite o novo preço de {novoproduto[1]}: ')
                        novoproduto[3] = novopreco
                        print("Preço atualizado!")
                else:
                    mudanca = int(input(f'Digite 1 para alterar o preço de {leite[1]}, 2 para alterar o preço de {papelhigienico[1]}, 3 para alterar o preço de {lencol[1]}: '))
                    if mudanca == 1:
                        novopreco = input("Digite o novo preço de ",leite[1],": ")
                        leite[3] = novopreco
                        print("Preço atualizado!")
                    if mudanca == 2:
                        novopreco = input(f'Digite o novo preço de {papelhigienico[1]}: ')
                        papelhigienico[3] = novopreco
                        print("Preço atualizado!")
                    if mudanca == 3:
                        novopreco = input(f'Digite o novo preço de {lencol[1]}: ')
                        lencol[3] = novopreco
                        print("Preço atualizado!")
            else:
                novoproduto = novoproduto
        elif funcao == 5: #SAIR
            exit()