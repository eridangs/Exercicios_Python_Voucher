print("DIGITE F, M ou O REFERENTE A INICIAL DO SEU SEXO ")
a = input(" ")
b = a.upper()
if  b=="F":
    print(f'SEXO FEMININO')
elif b=="M":
    print(f'SEXO: MASCULINO')
else:
    if b=="O":
        print(f'OUTROS')
    else:
        print('SEXO INVALIDO')    