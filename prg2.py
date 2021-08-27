import sys

def extended_euclidean(a, b):

    if(b == 0):
        return [1, 0]

    [x1, y1] = extended_euclidean(b, a%b)

    x = y1
    y = x1 - (a//b)*y1

    return [x, y]


def __main__():
    
    args = sys.argv
    print(args)
    a1 = int(args[1])
    b1 = int(args[2])
    
    a = max(a1, b1)
    b = min(a1, b1)
    
    [x, y] = extended_euclidean(a, b)   
    
    print(a, b)
    print(f"{x} {y}")


__main__()