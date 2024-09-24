from barbearia import Barbearia
from cliente_barbearia import Cliente
def Menu():
    print("Escolha qual serviço deseja:")
    print("1 - Agendar cliente\n2 - Cancelar cliente agendado\n3 - Visualizar clientes agendados")

barbearia = Barbearia()
while True:
    try:
        Menu()
        option = int(input(""))

        if option == 1:
            nome_cliente = input("Nome do cliente: ")
            data = input("Data escolhida pelo cliente: ")
            hora = input("Hora marcada pelo cliente: ")
            servico = input("Serviços escolhidos pelo cliente: ")
            agendado = Cliente(nome_cliente,data,hora,servico)
            barbearia.Agendar(agendado)

        if option == 2:
            nome_cliente_agendado = input("Nome do cliente agendado: ")
            barbearia.CancelarHorarioMarcado(nome_cliente_agendado)

        if option == 3:
            barbearia.MostrarClientesAgendados()

    except Exception as e:
        print(e)
