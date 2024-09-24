class Cliente:
    def __init__(self,nome,data,hora,servico):
        self.Nome = nome
        self.Data = data
        self.Hora = hora
        self.Serviço = servico
        self.Marcado = True

    def __str__(self) -> str:
        status = "Confirmado"
        if self.Marcado == False:
            status = "Cancelado"

        return f'{self.Nome} {self.Data} {self.Hora} {self.Serviço} - {status}'