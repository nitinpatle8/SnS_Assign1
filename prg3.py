# नितीन पटले
# 𝓑𝓣𝟣𝟪𝓒𝓢𝓔𝟢𝟢𝟦

import sys

# prime number is in the form 
# 6n ± 5
def product_of_primes(a):
    
    if a <= 1: return []
    
    l = []
    
    i = 2
    count = 0
    
    while (a%i == 0):
        a = a//i
        count += 1
    
    if(count > 0):
        l.append([i, count])
    
    i = 3
    count = 0
    
    while (a%i == 0):
        a = a//i
        count += 1
    
    if(count > 0):
        l.append([i, count])
    
    i = 5
    
    while i*i<=a:
        
        count = 0
        
        while(a%i == 0):
            a = a//i
            count+=1
        if count > 0:
            l.append([i, count])
        
        count = 0
        
        while(a%(i+2) == 0):
            a = a//(i+2)
            count+=1
        if count > 0:
            l.append([i+2, count])
           
        i+=6
        
    if a > 1:
        l.append([a, 1])

    return l

def __main__():
    
    args = sys.argv

    a = int(args[1])
    
    l = product_of_primes(a)

    for i in l:
        for j in range(i[1]):
            print(i[0], end=" ")
        
__main__()

