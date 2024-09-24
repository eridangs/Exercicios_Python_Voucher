ano_atual = int(input("Ano atual: "))
#representa o ano em que o percentual foi dobrado
aumento2ano = 1997
salario_inicio = 1000
aumento_inicial = 0.015
#representa 1996
salario_atual = salario_inicio + (salario_inicio * aumento_inicial)
percentual_aumento = 0.015 * 2
while aumento2ano < ano_atual:
    aumento2ano += 1
    salario_atual = salario_atual + (salario_atual * percentual_aumento)
    percentual_aumento *= 2
    print(aumento2ano)
    print(f'salario {salario_atual:.2f}') 
    #print(f'{percentual_aumento:.2f}')