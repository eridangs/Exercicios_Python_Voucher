class carro():
    cor = "sem cor"
    marca = "sem marca"
    modelo = "sem modelo"
    ano = 2010
    km_rodados = 0
    status_do_motor = False
    status_do_movimento = False
    def detalhes(self):
        print(f'{self.cor}')
        print(f'{self.marca}')
        print(f'{self.modelo}')
        print(f'{self.ano}')
        print(f'{self.km_rodados}')
        print(f'{self.status_do_motor}')
        print(f'{self.status_do_movimento}')
        
    def AdicionarKm(self,km):
        self.km_rodados += km

    def AdicionarMotor(self):
        if self.status_do_motor == False:
            self.status_do_motor = "Motor desligado"
            self.status_do_movimento = "Carro parado"
        elif self.status_do_motor == True:
                self.status_do_motor ="Motor ligado"
                opcao = input("Carro está ANDANDO ou PARADO? ")
                if opcao == "andando":
                    self.status_do_movimento = "Carro andando"
                elif opcao == "parado":
                    self.status_do_movimento = "Carro parado"
                    
        
    # def AdicionarMovimento(self):
    #     if self.status_do_movimento == False:
    #         self.status_do_movimento = "Carro parado"
    #     elif self.status_do_movimento == True:
    #         self.status_do_movimento = "Carro andando"

carro1 = carro()
carro1.cor = "Amarelo"
carro1.marca = "Honda"
carro1.modelo = "HR-V"
carro1.ano = 2024
carro1.AdicionarKm(int(input("Digite a quilometragem do carro: ")))
carro1.status_do_motor = True
carro1.AdicionarMotor()
carro1.detalhes()

carro2 = carro()
carro2.cor = "Vermalho"
carro2.marca = "Nissan"
carro2.modelo = "SUV"
carro2.ano = 2023
carro2.AdicionarKm(int(input("Digite o valor: ")))
carro2.status_do_motor = False
carro2.AdicionarMotor()
carro2.detalhes()