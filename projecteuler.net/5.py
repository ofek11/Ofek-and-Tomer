from functools import reduce
import math
def lcm(a,b):
    return a*b//math.gcd(a,b)
print(reduce(lcm,range(1,21)))