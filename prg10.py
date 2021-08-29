import sys

def gcd(a, b):
    if(a < b):
        return gcd(b, a)
    
    if(b == 0):
        return a
    
    return gcd(b, a%b)


def order_of_a_mod_m(a, m):
    
    phim = RRSM_count(m)

    for i in range(2, phim+1):
        
        if (phim%i == 0) and pow(a, i)%m == 1:
            return i
    
    return -1

def RRSM_count(m):
    
    # m = p1^alpha1 * p2^alpha2 * p3^alpha3 * .....
    # phi(m) = (p1^alpha1 - p1^(alpha1 - 1)) * (p2^alpha2 - p2^(alpha2 - 1)) * .....
    
    l = 0
    
    for i in range(0, m):
        if(gcd(i, m) == 1):
            l+=1

    return l

def primitive_roots(m):
    
    count = RRSM_count(RRSM_count(m))

    # [1, m-1]
    
    # []
    
    l = []
    
    phim = RRSM_count(m)
    
    g = 0
    
    for a in range(1, m):
        
        if(gcd(a, m) == 1):
            
            if(order_of_a_mod_m(a, m) == phim):
                
                g = a
                print(g)
                break
    
    print(phim)
    
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