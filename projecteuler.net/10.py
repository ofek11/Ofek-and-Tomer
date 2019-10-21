# https://projecteuler.net/problem=10
import time
import math


def is_prime_num(num):
    sq = int(math.sqrt(num))
    global primes
    for j in primes:
        if num % j == 0:
            return False
        elif j >= sq:
            break
    primes.append(num)
    return True


primes = [2]
start_time = time.time()
for number in range(2, 2000000):
    is_prime_num(number)
    if number % 10000 == 0:
        print(number)
print("--- %s seconds ---" % (time.time() - start_time))
print('Number of primes below 2,000,000:', sum(prime_numbers))
