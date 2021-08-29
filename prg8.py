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
    
    return (extended_euclidean(a//g, n//g)[0] + n)%n  


def system_of_congruences(a, b, m):
    
    M = 1
    n = len(a)
    
    # you also have to write for case where 
    # gcd(mi, mj) != 1 
    # then you will have to disintegrate mi, mj then check if any inconsistencies exists
    # lecture _09_08 
    
    for i in range(n):
        if(gcd(a[i], m[i]) > 1):
            return []
        for j in range(n):
            if (gcd(m[i], m[j]) > 1):
                return []
        
        M = i*M
                
    x = []
    
    for i in range(n):
        
        #(M//mi) * inverse(M//mi) * inverse(ai) * bi
        ai = (multiplicative_inverse(a[i]) * b[i])%m[i]
        
        xi = (M//m[i]) * multiplicative_inverse(M//m[i]) * ai)
        x.append(xi)
        
    return x

def __main__():
    
    args = sys.argv

    n = int(args[1])
    
    a = []
    b = []
    m = []
    
    for i in range(n):
        j = 3*i + 2
        a.append(int(args[j]))
        b.append(int(args[j+1]))
        m.append(int(args[j+2]))
        
    ans = system_of_congruences(a, b, m)
    
    if(len(ans) == 0):
        print("N")
    else:
        print("Y", end=" ")
        for i in ans:
            print(i, end=" ")
    

__main__()