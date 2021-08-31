# नितीन पटले
# 𝓑𝓣𝟣𝟪𝓒𝓢𝓔𝟢𝟢𝟦

import sys

def gcd(a, b):

    if(b == 0):
        return a
    
    return gcd(b, a%b)

# 𝞿(m)
# if i [1, m)
# if gcd(i, m) equals to 1
# then i is in RRSM (Residue System Modulo m)
def RRSM_m(m):
    
    l = []
    
    for i in range(0, m):
        if(gcd(i, m) == 1):
            l.append(i)

    return l

def __main__():
    
    args = sys.argv

    m = int(args[1])
    
    l = RRSM_m(m)
    
    for i in l:
        print(i,end=" ")
        
    print(len(l))
        
__main__()