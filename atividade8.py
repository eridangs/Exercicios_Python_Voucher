a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))
if a == b:
    print(f'Números iguais, insira apenas números diferentes entre si')
    exit()
if (a == c):
    print(f'Números iguais, insira apenas números diferentes entre si')
    exit()
if (b == c):
    print(f'Números iguais, insira apenas números diferentes entre si')
    exit()
elif a>b>c:
    print(f'{a},{b},{c}')
elif a>c>b:
    print(f'{a},{c},{b}')
elif b>c>a:
    print(f'{b},{c};{a}')
elif b>a>c:
    print(f'{b},{a},{c}')
elif c>b>a:
    print(f'{c},{b},{a}')
else:
    print(f'{c},{a},{b}')