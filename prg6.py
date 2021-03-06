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

def __main__():
    
    args = sys.argv

    a = int(args[1])
    
    n = int(args[2])
    
    ans = multiplicative_inverse(a, n)
    
    if(ans == -1):
        print("N", end="")
    else:
        print(f"Y {ans}", end="")
    
    
__main__()