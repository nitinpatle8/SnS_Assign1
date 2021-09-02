# नितीन पटले
# 𝓑𝓣𝟣𝟪𝓒𝓢𝓔𝟢𝟢𝟦

import sys

def gcd(a, b):
    
    if(b == 0):
        return a
    
    return gcd(b, a%b)

def gcd_list(l):
    
    n = len(l)
    
    if n == 0:
        return -1
    
    g = l[0]
 
    for i in range(1, n):
        g = gcd(g, l[i])
    
    return g

def product_of_primes(a):
    
    if a <= 1: 
    	return []
    
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

# method 1 brute force
def common_divisors_1(args, n):
	
	ret_val = []
	
	minimum = args[0]
	
	for i in args:
		minimum = min(i, minimum)
	
	for i in range(2, minimum+1):
		
		flag = 1

		for j in args:
			
			if(j%i != 0):
				flag = 0

		if(flag):
			ret_val.append(i)
	
	return ret_val		

# method 2 using gcd 

def common_divisors_2(args, n):
    
    if(n == 0):
        return []
    
    g = gcd_list(args)
    
    l = []
    
    for i in range(1, g+1):
        if(g % i == 0):
            l.append(i)
        
    return l

# method 3 using primitive roots 
# postponing this

# gcd_list takes list having atleast 1 integer
# returns -1 if empty list


def __main__():
	
    args = sys.argv
	
    n = int(args[1])
	
    l = [int(args[i]) for i in range(2, n+2)]
	
    l = common_divisors_2(l, n)

    m = len(l)
    
    for i in range(m-1):
        print(l[i], end=" ")
    
    if(m > 0):
        print(l[m-1], end="")

__main__()

