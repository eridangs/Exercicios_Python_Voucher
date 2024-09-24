a = float(input("digite o valor de a: "))
if a == 0:
    print("A equação não é do segundo grau")
    exit()
b = float(input("digite o valor de b: "))
c= float(input("digite o valor de c: "))
delta = ((b)**2 - 4*(a)*(c))
print(f'{delta}')
if delta <= 0 :
    x_only1 = (-b /2 * a)
    print("Há apenas 1 raiz real que é: ", x_only1)
else:     
    x_1 = (((-b) + (delta)** 0.5)/ (2* a))
    x_2 = (((-b) - (delta)** 0.5) /(2* a))
    print(f'{x_1}')
    print(f'Há duas raízes reais: {x_1} e {x_2}')