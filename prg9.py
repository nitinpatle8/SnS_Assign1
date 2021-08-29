
import sys


def gcd(a, b):
    if(a < b):
        return gcd(b, a)
    
    if(b == 0):
        return a
    
    return gcd(b, a%b)


# α, β, γ, δ, ε

def RRSM_count(m):
    
    # m = p1^alpha1 * p2^alpha2 * p3^alpha3 * .....
    # phi(m) = (p1^alpha1 - p1^(alpha1 - 1)) * (p2^alpha2 - p2^(alpha2 - 1)) * .....
    
    l = 0
    
    for i in range(0, m):
        if(gcd(i, m) == 1):
            l+=1

    return l


def order_of_a_mod_m(a, m):
    
    phim = RRSM_count(m)

    for i in range(2, phim+1):
        
        if (phim%i == 0) and pow(a, i)%m == 1:
            return i
    
    return -1

def __main__():
    
    args = sys.argv

    a = int(args[1])
    m = int(args[2])
    
    print(order_of_a_mod_m(a, m))
    

__main__()