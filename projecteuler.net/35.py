import math
import time
start_time = time.time()


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


def cal_circular_number(num):
    str_num = str(num)
    circular_numbers = [num]
    counter = ''
    for number in range(1, len(str_num)):
        counter = str_num[number:] + str_num[:number]
        circular_numbers.append(int(counter))
    return circular_numbers


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


def if_circular_prime(list_of_primes, circular_numbers):
    global Circular_primes
    for number in circular_numbers:
        if not binarySearch(primes, number):
            return False
    Circular_primes.append(circular_numbers[0])
    return True


primes = [2, ]
Circular_primes = []
for a in range(2, 1_000_000):
    is_prime_num(a)

for b in range(2, 1_000_000):
    circular_number = cal_circular_number(b)
    if_circular_prime(primes, circular_number)
    if b % 1_000 == 0:
        print(b)


print('circular primes below one million:', len(Circular_primes))
