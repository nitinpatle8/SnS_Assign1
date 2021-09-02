# नितीन पटले
# 𝓑𝓣𝟣𝟪𝓒𝓢𝓔𝟢𝟢𝟦

import sys

# a is considered greater than equal to b
def extended_euclidean(a, b):

    if(b == 0):
        return [1, 0]

    [x1, y1] = extended_euclidean(b, a%b)

    x = y1
    y = x1 - (a//b)*y1

    return [x, y]


def __main__():
    
    args = sys.argv
    
    a = int(args[1])
    b = int(args[2])
    
    [x, y] = extended_euclidean(a, b)   
    
    print(f"{x} {y}", end="")

__main__()