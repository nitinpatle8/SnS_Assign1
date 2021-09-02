# नितीन पटले
# 𝓑𝓣𝟣𝟪𝓒𝓢𝓔𝟢𝟢𝟦

import sys

# quotient and remainder on line number 134

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

# take out common factors 
# and then return ((a/(multiplication of common factors))^y mod n) * (multiplication of common factors mod n)
#   y = (|)(n) * q + r
#   (a/multiplication of common factors^(y%n)) * (multiplication of common factors mod n)
#   a/gcd ^ (y%n)) * (gcd)

def calculate_generalized_euler_thm(a, x, n):
    
    # take out common factors mod n 
    g = gcd(a, n)
    
    if(g == n): 
        return (0, -1, -1)

    phi = RRSM_count(n)
    
    # ((a//g)^x%phi ) * gcd^x
    
    # method 1 in which g^x is calculated 
    
    ans = ((pow(a//g, x%phi))%n * (pow(g, x))%n)%n 
    
    # print(f"quetient is {x//phi} ; remainder is {x%phi}", end=" ")
    quotient = x//phi
    remainder = x%phi
    
    # method 2 remaining minimise g^x
    
    return (ans, quotient, remainder)

def __main__():
    
    args = sys.argv

    a = int(args[1])
    
    x = int(args[2])
    
    n = int(args[3])
    
    # a^x mod n
    (ans, quotient, remainder) = calculate_generalized_euler_thm(a, x, n)
    
    print(ans, end="")
    
    # print(f"{quotient} {remainder}", end="")
    

__main__()