n = (input("Digite um número entre 0 e 999: "))
if int(n) < 0 and int(n) > 999 :
    print ("Número inválido")
    exit()
if int(n) >= 100 and int(n) <= 999:
    cent= int(n[0])
    deze = int(n[1])
    unid= int(n[2]) #print(f'{cent}, {deze}, {unid}')
    if cent == 1 and deze == 1 and unid == 1:
        print(f"{cent} centena, {deze} dezena e {unid} unidade")
    if cent == 1 and deze == 1 and (unid == 0 or unid >= 2):    
        print(f'{cent} centena, {deze} dezena e {unid} unidades')
    if cent == 1 and (deze == 0 or deze >= 2) and unid == 1:
        print(f'{cent} centena, {deze} dezenas e {unid} unidade')   
    if cent == 1 and (deze == 0 or deze >= 2) and (unid == 0 or unid >= 2):
        print(f'{cent} centena, {deze} dezenas e {unid} unidades')
        #ate aqui tudo certo
    if (cent >= 2) and deze == 1 and unid == 1:
        print(f"{cent} centenas, {deze} dezena e {unid} unidade")
    if (cent >= 2)  and deze == 1 and (unid == 0 or unid >= 2):    
        print(f'{cent} centenas, {deze} dezena e {unid} unidades')
    if (cent >= 2) and (deze == 0 or deze >= 2) and unid == 1:
        print(f'{cent} centenas, {deze} dezenas e {unid} unidade')   
    if (cent >= 2) and (deze == 0 or deze >= 2) and (unid == 0 or unid >= 2):
        print(f'{cent} centenas, {deze} dezenas e {unid} unidades')
        #ate aqui tudo certo
elif int(n) >= 10 and int(n) <= 99:
    dezena= int(n[0])
    unidade= int(n[1])
    if dezena == 1 and unidade == 1:
        print(f"{dezena} dezena e {unidade} unidade")
    if dezena == 1 and (unidade == 0 or unidade >= 2):  
        print(f"{dezena} dezena e {unidade} unidades")
    if dezena >= 2 and unidade == 1:
        print(f"{dezena} dezenas e {unidade} unidade")
    if dezena >= 2 and (unidade == 0 or unidade >= 2): 
        print(f'{dezena} dezenas e {unidade} unidades')
elif int(n) <= 9:
    unidade1 = int(n[0])
    if unidade1 == 1:
        print(f'{unidade1} unidade')
    else:
        print(f'{unidade1} unidades')



