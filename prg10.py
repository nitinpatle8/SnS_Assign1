# नितीन पटले
# 𝓑𝓣𝟣𝟪𝓒𝓢𝓔𝟢𝟢𝟦

import sys

def gcd(a, b):

    if(b == 0):
        return a
    
    return gcd(b, a%b)

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

def order_of_a_mod_m(a, m):
    
    phim = RRSM_count(m)

    for i in range(2, phim+1):
        
        if (phim%i == 0) and pow(a, i)%m == 1:
            return i
    
    return -1

def RRSM_count(m):
    
    # m = p1^𝝰1 * p2^𝝰2 * p3^𝝰3 * ...
    # 𝞅(m) = (p1^𝝰1 - p1^(𝝰1 - 1)) * (p2^𝝰2 - p2^(𝝰2 - 1)) * .....
    
    phi = 1
    
    # method 1 : brute force 
    # for i in range(0, m):
    #     if(gcd(i, m) == 1):
    #         phi+=1

    # method 2 : euler's totient function + multiplicity of m
    
    l = product_of_primes(m)
    
    for i in l:
        phi *= pow(i[0], i[1]) - pow(i[0], i[1] - 1)
    
    return phi

def primitive_roots(m):
    
    # count = RRSM_count(RRSM_count(m))

    # [1, m-1]
    
    # []
    
    l = []
    
    phim = RRSM_count(m)
    
    g = 0
    
    # primitive root will be in range [1, m)
    
    for a in range(1, m):
        
        if(gcd(a, m) == 1):
            
            if(order_of_a_mod_m(a, m) == phim):
                
                g = a
                # print(g)
                break
    
    # print(phim)
    
    # p
    # p^(something which is relatively prime to phi)
    
    # range of power => [1, phi)
    
    if(g > 0):
        
        for i in range(1, phim):
            
            if(gcd(i, phim) == 1):
                l.append(pow(g, i))
                
    return l


def __main__():
    
    args = sys.argv

    m = int(args[1])
    
    l = primitive_roots(m)
    
    print(len(l), end=" ")
    
    for i in l:
        print(i, end=" ")


__main__()