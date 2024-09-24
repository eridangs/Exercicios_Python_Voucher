data = (input("Digite uma data de nascimento no formato dd/mm/aaaa: "))
if data[2] == "/" and data[5] == "/" :
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6: ])
    if 31 >= dia and dia > 0 and 12 >= mes and mes > 0 and 9999 >= ano and ano >= 1000:
        print("data válida")
    else:
        print("data invalida")
else:
    print("Formato digitado invalido, certifique que a data inserida corresponde ao formato dd/mm/aaaa.")