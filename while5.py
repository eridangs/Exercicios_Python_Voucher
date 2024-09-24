while True:
    nome = input("Digite um nome com mais que três letras: ")
    idade = int(input("Digite uma idade entre 0 e 150: "))
    salario = float(input("Digite um salario: "))
    sexo = input("Digite 'f' para feminino, 'm' para masculino ou 'o' para outros: ")
    estado_civil = input("Digite 's' para solteiro, 'c' para casado, 'v' para viuvo ou 'd' para divorciado: ")
    if nome == nome[0:3]:
        # if idade >= 0 and idade <= 150 and salario > 0 and sexo == "f" or "m" or "o" and estado_civil == "s" or "c" or "v" or "d":
        print("Nome com até 3 digitos, insira um nome com mais que três letras.")
    else:
        if idade >= 0 and idade <= 150 and salario > 0 and sexo == "f" or "m" or "o" and estado_civil == "s" or "c" or "v" or "d":
            print("Obrigado por fornecer os dados!")
            break
# nome = input()
# if nome == nome[0:3]:
#     print("nome 3 digitos")