import time

start_time = time.time()


def is_prime_num(num):
    import math
    i = 1
    for i in range(1, int(math.sqrt(num + 1))):
        i += 1
        if num % i == 0:
            return False
    return True


number = 0
counter = 0
while counter != 10_001:
    number += 1
    if is_prime_num(number):
        counter += 1
print("--- %s seconds ---" % (time.time() - start_time))
print('number of prime below 10:', number)
