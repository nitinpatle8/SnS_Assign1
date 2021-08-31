
# 3^x mod 21 

def RRSM_count1(m):
    
    # m = p1^𝝰1 * p2^𝝰2 * p3^𝝰3 * ...
    # 𝞅(m) = (p1^𝝰1 - p1^(𝝰1 - 1)) * (p2^𝝰2 - p2^(𝝰2 - 1)) * .....
    
    phi = 0
    
    # method 1 : brute force 
    for i in range(1, m):
        if(gcd(i, m) == 1):
            phi+=1

    # method 2 : euler's totient function + multiplicity of m
    
    # l = product_of_primes(m)
    
    # for i in l:
    #     phi += pow(i[0], i[1]) - pow(i[0], i[1] - 1)
    
    return phi

def RRSM_count2(m):
    
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

def gcd(a, b):    
    if(b == 0):
        return a
    
    return gcd(b, a%b)

# for i in range(2, 10000):
#     if(RRSM_count1(i) != RRSM_count2(i)):
#         print(f"{i} {RRSM_count1(i)} {RRSM_count2(i)}")
        
print(RRSM_count1(6))