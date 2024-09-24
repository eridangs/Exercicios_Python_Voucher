while True:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == senha:
        print("Erro, senha não pode ser igual a usuário.")
    else:
        break