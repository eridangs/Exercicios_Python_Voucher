M_altura=0
M_peso=0
m_altura= 5
m_peso=500
clientes = 0
mediaAltura = 0
mediaPeso = 0
while True:
    codigo = int(input("Digite seu código ou 0 para parar: "))
    peso = float(input("Digite seu peso em KG: "))
    altura = float(input("Digite sua altura em Metros: "))
    mediaPeso+= peso
    mediaAltura+= altura
    clientes+= 1
    if peso > M_peso:
        M_peso= peso
        codigo_maisgordo = codigo
    #print(M_peso, codigo_maisgordo)
    if peso < m_peso:
        m_peso= peso
        codigo_maismagro = codigo
    #print(m_peso, codigo_maismagro)
    if altura> M_altura:
        M_altura= altura
        codigo_maisalto = codigo
    #print(M_altura, codigo_maisalto)
    if altura< m_altura:
        m_altura= altura
        codigo_maisbaixo = codigo
    #print({m_altura, codigo_maisbaixo})
    if codigo == 0:
        print(f'Média dos pesos: {(mediaPeso/clientes)}')
        print(f'Média das alturas: {(mediaAltura/clientes)}')
        print(f'O maior peso é {M_peso}kg que pertence ao cliente com o código {codigo_maisgordo}.')
        print(f'O menor peso é {m_peso}kg que pertence ao cliente com o código {codigo_maismagro}.')
        print(f'A maior altura é {M_altura}m que pertence ao cliente com o código {codigo_maisalto}')
        print(f'A menor altura é {m_altura}m que pertence ao cliente com o código {codigo_maisbaixo}')
        break


# while True:
#     altura = 0
#     comparacao= altura
#     codigo= 1
#     while codigo != 0:
#         codigo = int(input("Digite seu código ou 0 para parar: "))
#         peso = float(input("Digite seu peso em KG: "))
#         altura = float(input("Digite sua altura em Metros: "))
#         if altura > comparacao:
#             comparacao = altura
#             cod_alto = codigo
#             print("A altura maior é" ,altura,"m e usuário com codigo",cod_alto)
#             break
#         if altura < comparacao:
#             comparacao = altura
#             cod_baixo = codigo
#             print("A altura menor é" ,altura,"m e usuário com codigo",cod_baixo)
#             break
#         clientes+= 1
        # M_peso+= peso
        # M_altura+= altura
        #  if codigo == 0:
        #      print(f'Média dos pesos: {(M_peso/clientes)}')
        #      print(f'Média das alturas: {(M_altura/clientes)}')
        #      break