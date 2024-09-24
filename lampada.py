def Area():
    l = float(input("Digite a largura do cômodo: "))
    c = float(input("Comprimento do cômodo: "))
    area = l * c
    return area
def menu():
    print("Tipo do cômodo\n-1 - Sair\n0 - 12Watts\n1 - 15Watts\n2 - 18Watts\n3 - 20Watts\n4 - 22Watts")
def QuantLampadas():
    lampadas = (Area() * tipo) / 60
    print("A quantidade necessária de lâmpadas é",lampadas)
    return lampadas
while True:
    menu()
    tipo = int(input("Escolha: "))
    if tipo == 0:
        tipo = 12
        QuantLampadas()
    elif tipo == 1:
        tipo = 15
        QuantLampadas()
    elif tipo == 2:
        tipo = 18
        QuantLampadas()
    elif tipo == 3:
        tipo = 20
        QuantLampadas()
    elif tipo == 4:
        tipo = 22
        QuantLampadas()
    elif tipo == -1:
        break