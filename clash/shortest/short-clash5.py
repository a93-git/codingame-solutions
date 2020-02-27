""" Print the sum of the prime factors of a number"""

import sys
import math

n = int(input())
def primeFactors(n): 
    retval = []  
    while n % 2 == 0: 
        retval.append(2) 
        n = n / 2 
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            retval.append(i) 
            n = n / i 
    if n > 2: 
        retval.append(n)
    return retval
print(int(sum(primeFactors(n))))