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

# method 1 improvement needed according to the issue raised
def system_of_congruences_1(a, b, m):
    
    M = 1
    n = len(a)
    
    # you also have to write for case where 
    # gcd(mi, mj) != 1 
    # then you will have to disintegrate mi, mj then check if any inconsistencies exists
    # lecture _09_08 

    # print("before loop")
    
    for i in range(n):
        
        if(b[i] % gcd(a[i], m[i]) != 0):
            return []
        
        # gcd(m[i], m[j]) > 1 currently is wrong 
        # need to be improvised
        for j in range(n):
            if i!=j and (gcd(m[i], m[j]) > 1):
                return []
        
        M = m[i]*M
    
    x = []
    
    for i in range(n):
        
        #(M//mi) * inverse(M//mi) * inverse(ai) * bi
        ai = (multiplicative_inverse(a[i], m[i]) * b[i])%m[i]
        
        xi = (M//m[i]) * multiplicative_inverse(M//m[i], m[i]) * ai
        
        x.append(xi)
        
    return x

# method 2 needs improvement
# def system_of_congruences_2(a, b, m):
    
#     M = 1
#     n = len(a)
    
#     if(n == 0):
#         return []
    
#     for i in range(n):
#         if b[i]%gcd(a[i], m[i])!=0:
#             return []
            
#     x = solutions_of_congruence(a[0], b[0], m[0])
    
#     l = []
    
#     for i in x:
#         flag = 1
#         for j in range(n):
#             if((a[j]*i)%m[j] != b):
#                 flag = 0
#                 break
#         if flag == 1:
#             l.append(i)
            
#     return l

def __main__():
    
    args = sys.argv

    n = int(args[1])
    
    a = []
    b = []
    m = []
    
    for i in range(n):
        a.append(int(args[3*i + 2]))
        b.append(int(args[3*i + 3]))
        m.append(int(args[3*i + 4]))
    
    ans = system_of_congruences_1(a, b, m)
    
    if(len(ans) == 0):
        print("N")
    else:
        print("Y", end=" ")
        n = len(ans)
        for i in range(n-1):
            print(ans[i], end=" ")
        print(ans[n-1], end="")

__main__()