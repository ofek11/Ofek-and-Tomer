import math


def is_prime_num(num):
    if num == 1:
        return True
    sq = int(math.sqrt(num))
    global primes
    for j in primes:
        if num % j == 0:
            return False
        elif j >= sq:
            break
    primes.append(num)
    return True


def circular_number(num):
    str_num = str(num)
    circular_numbers = [num]
    counter = ''
    for number in range(1, len(str_num)):
        counter = str_num[number:] + str_num[:number]
        if counter == str_num:
            break
        circular_numbers.append(int(counter))
    return circular_numbers


valid = True
primes = [2]
Circular_primes = [2]
for n in range(2, 1_000):
    Circular_numbers = circular_number(n)
    for b in Circular_numbers:
        if not is_prime_num(b):
            valid = False
    if valid:
        Circular_primes.append(n)
    valid = True
print(len(Circular_primes))
