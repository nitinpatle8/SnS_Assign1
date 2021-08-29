import sys

def gcd(a, b):
    if(a < b):
        return gcd(b, a)
    
    if(b == 0):
        return a
    
    return gcd(b, a%b)

def RRSM_count(m):
    
    # m = p1^alpha1 * p2^alpha2 * p3^alpha3 * .....
    # phi(m) = (p1^alpha1 - p1^(alpha1 - 1)) * (p2^alpha2 - p2^(alpha2 - 1)) * .....
    
    l = 0
    
    for i in range(0, m):
        if(gcd(i, m) == 1):
            l+=1

    return l
# take out common factors and then return ((a/(multiplication of common factors))^y mod n) * (multiplication of common factors mod n)
# ---------------------------------------=> y = (|)(n) * q + r
# ---------------------------------------=> (a/multiplication of common factors^(y%n)) * (multiplication of common factors mod n)
# ---------------------------------------=> (a/gcd ^ (y%n)) * (gcd)
def calculate_generalized_euler_thm(a, x, n):
    
    # take out common factors mod n 
    g = gcd(a, n)
    
    if(g == n): 
        return 0

    phi = RRSM_count(n)
    
    
    ans = ((pow(a//g, x%phi))%n * (pow(g, x))%n)%n 
    
    return ans

def __main__():
    
    args = sys.argv

    #a = int(args[1])
    
    #x = int(args[2])
    
    #n = int(args[3])
    
    # a^x mod n
    flag = 1
    for a in range(1, 100):
        for x in range(1, 100):
            for n in range(1, 10000):
                ans = calculate_generalized_euler_thm(a, x, n)
                if(pow(a, x)%n != ans):
                    flag = 0
                    print("program is incorrect")
    # print(ans)
    if(flag):
        print("program is correct")
    # print(pow(a, x)%n)
    
__main__()