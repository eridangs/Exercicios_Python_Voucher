a = 1
b = 2
c = 3
ehtriangular = False
num = int(input("Digite um número: "))
while (a * b * c) <= num:    
    if num == (a * b * c):
        ehtriangular = True
        #print("É um número triangular")
        break
    elif num != (a * b * c) :
        a += 1
        b += 1
        c += 1
if ehtriangular == True:
    print("é triangular")
else:
    print("não é triangular")