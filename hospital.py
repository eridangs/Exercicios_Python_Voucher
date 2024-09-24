print("Seja bem vindo ao Hospital Love!")
pacientes = []
nomes = []
if True == True:
    while True:  
        menu = input("Digite 1 para entrar como usuário, 2 para entrar como médico ou qualquer tecla para sair: ")
        if menu == "1":       
            infos = {}
            print("Voçê está na parte do usuário.\nAqui podes marcar consultas e visualizar seu histórico de consultas. ")
            opcao = int(input("Digite 1 para marcar uma consulta, 2 para visualizar histórico: "))
            if opcao == 1:
                nome =  input("Nome: ")
                infos["Nome do paciente"] = nome
                infos["CPF"] = input("CPF: ")
                infos["Idade"] = int(input("Idade: "))
                infos["Horario da consulta"] = input("Horario da consulta: ")
                print("Consulta agendada com sucesso.")
                pacientes.append(infos)
                nomes.append(nome)
            if opcao == 2:
                if pacientes != []:
                    for pessoa in pacientes:
                        print(f'{pessoa["Nome do paciente"]} tem uma consulta marcada para às {pessoa["Horario da consulta"]}h.')
                if pacientes == []: 
                    print("Voçê não tem nenhuma consulta passada ou futura.")
        if menu == "2":
            opcao = int(input("Olá médico. Digite 1 para visualizar lista de pacientes ou 2 para realizar consulta: "))
            if opcao == 1:
                if pacientes != []:
                    print(f'Pacientes com consultas marcadas: {pacientes}')
                else:
                    print("Não há pacientes marcados.")
            if opcao == 2:
                if pacientes != []:
                    atende = input(f'Qual o nome do paciente? ')
                    for nome in pacientes:
                        if atende == nomes[0]:
                            pacientes.pop(0)
                            print(nomes[0],"realizou a consulta.")
                        elif atende == nomes[1]:
                            pacientes.pop(1)
                            print(nomes[1],"realizou a consulta.")
                        elif atende == nomes[2]:
                            pacientes.pop(2)
                            print(nomes[2],"realizou a consulta.")
                else:
                    print("Não há consultas para hoje.")
        elif menu != 1 and menu != 2:
            exit()