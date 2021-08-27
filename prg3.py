import sys

def product_of_primes(a):
    
    if a <= 1: return [a]
    
    l = []
    i = 2
    
    while(a!=1):
        if a%i == 0:
            a = a//i
            l.append(i)   
        else:
            i+=1   

    return l

def __main__():
    
    args = sys.argv

    a = int(args[1])
    
    l = product_of_primes(a)

    for i in l:
        print(i, end=" ")
        
__main__()

