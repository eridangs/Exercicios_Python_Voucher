lampada = False
while True:
    def ligarlampada():
        Ligada = True
        return Ligada

    def desligarlampada():
        Desligada = False
        return Desligada

    a= int(input("1-Ligar lampada\n2-Desligar lampada\n3-Consultar:\n"))
    if a == 1:
        print(ligarlampada())
    elif a == 2:
        print(desligarlampada())
    elif a == 3:
        if lampada == True:
            print("Ligada")
        else:
            print("Desligada")
