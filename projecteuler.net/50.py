import math


def binarySearch(array, value):
    array = sorted(array)
    first = 0
    last = len(array) - 1

    while first <= last:
        midIndex = (first + last) // 2
        midValue = array[midIndex]

        if value == midValue:
            return True
        if value < midValue:
            last = midIndex - 1
        if value > midValue:
            first = midIndex + 1
    return False


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
max_prime = 0
counter = 0
limit = 1_000_000
max_counter = 0
for number in range(2, limit):
    is_prime_num(number)

for prime in primes:
    prime_sum = prime
    counter += 1
    prime_counter = 1
    for n in primes[counter:]:
        if prime_sum > limit:
            break
        if binarySearch(primes, prime_sum) and prime_sum > max_prime < limit and prime_counter > max_counter:
            max_counter = prime_counter
            max_prime = prime_sum
        prime_sum += n
        prime_counter += 1
print('Largest primes below 1,000,000 written as consecutive primes is:', max_prime)
