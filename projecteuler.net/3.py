import math


def is_prime_num(num):
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
c = None
s = 600_851_475_143
for number in range(2, s):
    if is_prime_num(number) and s % number == 0:
        s = int(s/number)
    if s == 1:
        break
print('finised:', number)