print("Insira seu nome, número e saldo da conta")
infos = {"Nome": "" , "Número": "", "Saldo": "" }
infos["Nome"] = input("Nome: ")
infos["Número"] = int(input("Número: "))
infos["Saldo"] = float(input("Saldo da conta: "))
print(infos)