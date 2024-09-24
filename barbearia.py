class Barbearia:
    def __init__(self):
        self.Gerenciamentos = []

    def Agendar(self,agendado):
        self.Gerenciamentos.append(agendado)

    def MostrarClientesAgendados(self):
        for i in self.Gerenciamentos:
            print(i)

    def CancelarHorarioMarcado(self,nome):
        cliente = self.BuscarCliente(nome)
        if cliente:
            if cliente.Marcado == True:
                cliente.Marcado = False
                print(f"Agendamento do cliente {nome} cancelado.")
            else:
                print(f"Horário do cliente {nome} já foi cancelado. ")
        else:
            print(f"Não foi encontrado cliente {nome} no sistema.")


    def BuscarCliente(self,nome):
        for cliente in self.Gerenciamentos:
            if cliente.Nome == nome:
                return cliente