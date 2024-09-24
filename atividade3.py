salario_atual= float(input("Salário atual:"))
if salario_atual<500:
    a = salario_atual+(salario_atual*0.15)
    print(a, "é o salário reajustado")
elif salario_atual<=1000:
    b = salario_atual+(salario_atual*0.10)
    print(f'{b} é o salario reajustado')
else:
    c = salario_atual+(salario_atual*0.05)
    print(f'{c} é o salário reajustado')