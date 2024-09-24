A=[5,9,10,-1,14,23,6,30]
cont=0
s= 0
for x in range(len(A)):
    if(A[x])%2==0:
        s+=(A[x])  
print(s)
## DEU CERTO
for i in A:
    if i % 2 == 0:
        s += i
print(s)
## DEU CERTO
while (cont < len(A)):
    if A[cont] % 2 == 0:
        s+= A[cont]
    cont+=1
print(s)
B=["a","b","c"]
for x in range(len(B)):
    print(x,(B[x]))