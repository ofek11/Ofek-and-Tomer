#https://projecteuler.net/problem=10
def is_prime_num(num):
    import math
    i=1
    for i in range(1,int(math.sqrt(num+1))):
        i+=1
        if num%i==0:
            return False
    return True

counter=0
for i in range(1,2_000_000):
    if is_prime_num(i):
        counter+=i
    print(i)
print('Number of primes below 2,000,000',counter)
