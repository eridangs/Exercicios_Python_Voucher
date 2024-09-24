valores = {}
for i in range(1):
    valores["Nota_1"] = float(input("Nota 1: "))
    valores["Nota_2"] = float(input("Nota 2: "))
    valores["Nota_3"] = float(input("Nota 3: "))
    valores["Nota_4"] = float(input("Nota 4: "))
    print(valores,(valores["Nota_1"]+valores["Nota_2"]+valores["Nota_3"]+valores["Nota_4"])/4)