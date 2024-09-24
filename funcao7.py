lista = [1,2,3,4,5,6,7,8,9,10]

def par():
        Par = 0
        for i in lista:      
            if i% 2 == 0:
                Par += i
        return Par
        
def impar():
        impar = 0
        for i in lista:      
            if i%2 != 0:
                impar += i
        return impar
        

print(f'{par()}')
print(f'{impar()}')
        
    
