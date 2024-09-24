saque = int(input("Qual o valor do saque? "))
if saque >= 10 and saque <= 600:
    cem = saque // 100
    saque %= 100
    cinq = saque // 50
    saque %= 50
    dez = saque // 10
    saque %= 10
    cinco = saque // 5
    saque %= 5
    um = saque // 1
    print (f'{cem} nota(s) de 100, {cinq} nota(s) de 50, {dez} nota(s) de 10, {cinco} nota(s) de 5 e {um} nota(s) de 1')
else:
    print("O valor do saque não atende ao valor mínimo ou máximo.")
    exit()