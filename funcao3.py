def exibeMenu():
    print("##### MENU #####\n")
    print("0- SAIR\n")
    print("1- SOMAR\n")
    print("2- SUBTRAIR\n")
    print("3- MULTIPLICAR\n")
    print("4- DIVIDIR\n")
    opcao = int(input("Escolha uma opção: "))
    return opcao

def somar(num1,num2):
    resultado = num1+num2
    return resultado

def subtrair(num1,num2):
    resultado = num1 - num2
    return resultado

def multiplicar(num1,num2):
    resultado = num1*num2
    return resultado

def dividir(num1,num2):
    resultado = num1/num2
    return resultado



i=0
opcao = 1
num1 =0
num2 =0
resultado=0

while opcao != 0:
    opcao= exibeMenu()
    if opcao <= 0:
        break

    num1= float(input("Informe o primeiro número para a operação: "))
    num2= float(input("Informe o segundo número para a operação: "))
    if opcao == 1:
        print("Resultado: ", somar(num1,num2))
    
    elif opcao == 2:
        print("Resultado: ",subtrair(num1,num2))

    elif opcao == 3:
        print("Resultado: ",multiplicar(num1,num2))

    elif opcao == 4:
        resultado = dividir(num1,num2)
        print("Resultado: %f\n\n" %resultado)