import sys

# नितीन पटले


def common_divisors(args, n):
	
	ret_val = []
	
	minimum = args[0]
	
	for i in range(0, n):
		minimum = min(args[i], minimum)
	
	for i in range(2, minimum+1):
		
		flag = 1

		for j in range(0, n):
			
			if(args[j]%i != 0):
				flag = 0

		if(flag):
			ret_val.append(i)
	
	return ret_val		

def __main__():
	
	args = sys.argv
	
	n = int(args[1])
	
	l = [int(args[i]) for i in range(2, n+2)]
	
	#print(l)

	l = common_divisors(l, n)
	
	for i in l:
		print(i, end=" ")


__main__()

