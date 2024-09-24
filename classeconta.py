class Conta_Corrente():
    def __init__(self,nome,cpf,numero,saldo):
        self.Nome = nome
        self.CPF = cpf
        self.Numero_conta = numero
        self.Saldo = saldo
        self.Movimento = 0

    def Mostrar(self):
        print(f'Olá {self.Nome}, aqui você pode gerenciar sua conta!')
        print(f'Nome: {self.Nome}\nNúmero da conta: {self.Numero_conta}\nSaldo da conta: {self.Saldo}')

    def Movimentacao(self):
        self.Movimento = int(input("Tecle 0 para sair, 1 para sacar ou 2 para depositar: "))
        if self.Movimento == 1:
            if self.Saldo > 0:
                valorsaque = float(input("Digite o valor que deseja sacar: "))
                if valorsaque <= self.Saldo:
                    self.Saldo -= valorsaque
                    print("Saque realizado!")
                elif valorsaque > self.Saldo:
                    print("O valor que deseja sacar é superior ao saldo disponível em sua conta.")
            elif self.Saldo <= 0:
                print("Não há um saldo positivo na conta disponível para saque.")
        if self.Movimento == 2:
            valordeposito = float(input("Digite o valor que deseja depositar: "))
            self.Saldo += valordeposito
            print("Deposito realizado!")

pessoa1 = Conta_Corrente("Lara Eridan","087.937.681-33","2201",200)
pessoa1.Mostrar()
pessoa1.Movimentacao()
pessoa1.Mostrar()

class Funcionario():
    def __init__ (self,nome,sobrenome,horas_trabalhadas,valor_hora,hora_extra):
        self.Nome = nome
        self.Sobrenome = sobrenome
        self.Horas_Trabalhadas = horas_trabalhadas
        self.Valor_Hora = valor_hora
        self.Horas_incrementadas = hora_extra

    def Metodos(self):
        print(f'Funcionário: {self.Nome} {self.Sobrenome}')
        print(f'Salário do mês: {self.Horas_Trabalhadas*self.Valor_Hora}')

    def Incrementacao_horas(self):
        self.Horas_Trabalhadas += self.Horas_incrementadas

funcionario1 = Funcionario("Lara","Genes",20,35,4)
funcionario1.Incrementacao_horas()
funcionario1.Metodos()




