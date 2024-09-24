#verificar se uma letra digitada é vogal ou consoante
letra = input("Digite uma letra: ")
letra = letra.lower()
if letra == "a" or "e" or "i" or "o" or "u":
    print(f'{letra} é uma  vogal')
else:
    print(f'{letra} é uma consoante')