# https://projecteuler.net/problem=10
import time


def is_prime_num(num):
    import math
    sq = int(math.sqrt(num))
    global prime_numbers
    for j in prime_numbers:
        if num % j == 0:
            return False
        elif j >= sq:
            break
    prime_numbers.append(num)
    return True


prime_numbers = [2]
start_time = time.time()
for number in range(2, 2000000):
    is_prime_num(number)
    if number % 10000 == 0:
        print(number)
print("--- %s seconds ---" % (time.time() - start_time))
print('Number of primes below 2,000,000:', sum(prime_numbers))
