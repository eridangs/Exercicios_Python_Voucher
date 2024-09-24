TAREFASTODO = []
codigo = -1
while True:
    adicionar = {}
    print("Gerencie suas tarefas!")
    opcao = int(input("Tecle 1- para adicionar tarefa\nTecle 2- para listar tarefas\nTecle 3- para marcar tarefa como concluída\nTecle 4- para remover tarefa\nTecle 5- para sair\n:"))
    if opcao == 1:
        adicionar["Código"]= codigo + 1
        adicionar["Tarefa"]= input("Tarefa a fazer: ")
        adicionar["Descrição"]= input("Descreva a tarefa: ")
        adicionar["Status"]= "Não concluída"
        TAREFASTODO.append(adicionar)
        codigo += 1
    elif opcao == 2:
        print(TAREFASTODO)
        if TAREFASTODO == []:
            print("Não há tarefas listadas.")
    elif opcao == 3:
        print(TAREFASTODO)
        concluir = input(f'Qual tarefa quer concluir? ')
        for tarefas in TAREFASTODO:
            if concluir == tarefas["Tarefa"]:
                tarefas["Status"] = "Concluída"
    elif opcao == 4:
        print(TAREFASTODO)
        remover = int(input(f'Qual o código da tarefa que deseja remover? '))
        for deleta in TAREFASTODO:
            TAREFASTODO.pop(deleta)
    elif opcao == 5:
        exit()