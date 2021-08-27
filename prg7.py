import sys

def gcd(a, b):
    if(a < b):
        return gcd(b, a)
    
    if(b == 0):
        return a
    
    return gcd(b, a%b)

def extended_euclidean(a, b):

    if(b == 0):
        return [1, 0]

    [x1, y1] = extended_euclidean(b, a%b)

    x = y1
    y = x1 - (a//b)*y1

    return [x, y]


def multiplicative_inverse(a, n):
    
    g = gcd(a, n)
    if(g != 1): 
        return -1
    
    return (extended_euclidean(a, n)[0] + n)%n  


def solutions_of_congruence(a, b, m):
    
    g = gcd(a, m)
    
    if(b % g != 0):
        return []
    
    l = []
    
    # alpha, beta, meu
    alpha = a//g
    beta = b//g
    meu = m//g
    
    print(f"{alpha} {beta} {meu}")
    
    alpha_inverse = multiplicative_inverse(alpha, meu)
    
    print(f"{alpha_inverse}")
    x = (alpha_inverse*beta)%meu
    
    for k in range(g):
        l.append(int(x + k * (m//g)))
    # x = beta * (alpha)^-1 (mod meu)
    return l


def __main__():
    
    args = sys.argv

    a = int(args[1])
    
    b = int(args[2])
    
    m = int(args[3])
    
    ans = solutions_of_congruence(a, b, m)
    
    if(len(ans) == 0):
        print("N")
    else:
        print("Y", end=" ")
        for i in ans:
            print(i, end=" ")
    

__main__()