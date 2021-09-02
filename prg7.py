# नितीन पटले
# 𝓑𝓣𝟣𝟪𝓒𝓢𝓔𝟢𝟢𝟦

import sys

def gcd(a, b):
    
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
    
    return (extended_euclidean(a//g, n//g)[0] + n)%n  


def solutions_of_congruence(a, b, m):
    
    g = gcd(a, m)
    
    # if g | b then solution does not exist
    if(b % g != 0):
        return []
    
    l = []
    
    # 𝝰, 𝝱, 𝝻
    alpha = a//g
    beta = b//g
    meu = m//g
    
    # generator = (𝝱 * 𝝰⁻¹) % 𝝻
    alpha_inverse = multiplicative_inverse(alpha, meu)
    
    # print(f"{alpha_inverse}")
    x = (alpha_inverse*beta)%meu
    
    # x can also be written as 
    # b * inverse(a) is not solution sir had earlier written wrong but then corrected it
    
    # generator + k * (m//gcd)
    # no of solutions = 𝞅(𝞅(m))
    
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
        n = len(ans)
        for i in range(n-1):
            print(ans[i], end=" ")
        print(ans[n-1], end="")

__main__()