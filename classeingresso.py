class Ingressos:
    def __init__(self,setor,preco):
        self.Setor = setor
        self.Preco = preco

    def __Changeprice(self): #Privado
        self.Novopreco = float(input("Novo preço: "))
        print("Preço foi alterado com sucesso.")

    def GetChangeprice(self): #Pegar função privada
        return self.__Changeprice()
    
    def Show_detalhes(self):
        print(f"Setor: {self.Setor}\nPreço: {self.Preco}")

class Vip(Ingressos):
    def __init__(self, setor, preco):
        super().__init__(setor, preco)
        self.Camarote = True
        self.Open_bar = True
        self.Open_food = True
        self.Estacionamento = True

    def Descricao(self):
        print("Benefícios do ingresso VIP:")
        self.Show_detalhes()

    def Pegar_bebida(self):
        if self.Open_bar == True:
            print("Retirada de bebida permitido.")

    def Acessar_camarote(self):
        if self.Camarote == True:
            print("Acesso ao camarote permitido.")

ingressoVip = Vip("Sertanejo", 250)
ingressoVip.Descricao()
ingressoVip.Pegar_bebida()
ingressoVip.Acessar_camarote()

manutencao = Ingressos("Rock",200)
manutencao.Show_detalhes()
manutencao.GetChangeprice()