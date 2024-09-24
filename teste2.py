funcionarios = []
maior = 0
for i in range(4):
    plural = {}
    plural["Nome"] = input("Nome: ")
    plural["Funcao"] = input("Função: ")
    plural["Salario"] = float(input("Salário: "))
    if plural["Salario"] > maior:
        maior = plural["Salario"]
    funcionarios.append(plural)
for pessoa in funcionarios:
    if pessoa["Salario"] == maior:
        print(f'Pessoa com maior salário é {pessoa["Nome"]} com o salário de {maior}.')
# for i in funcionarios:
#     if funcionarios[i]["Salario"] > maior:
#         maior = funcionarios[i]["Salario"]
#         print(funcionarios,maior)
    # elif funcionarios[1]["Salario"] >= 3000:
    #     print(funcionarios["Salario"])
    # elif funcionarios[2]["Salario"] >= 3000:
    #     print(funcionarios["Salario"])
    # elif funcionarios[3]["Salario"] >= 3000:
    #     print(funcionarios["Salario"])