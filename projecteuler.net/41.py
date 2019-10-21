import math


def is_prime_num(num):
    sq = int(math.sqrt(num))
    for j in range(2, sq):
        if num % j == 0:
            return False
    return True


def if_Pandigital_number(num):
    l_digits = []
    str_num = str(num)
    c = 0
    for digit in str_num:
        if digit in l_digits:
            return False
        else:
            l_digits.append(int(digit))
    l_digits.sort()
    for digit in l_digits:
        c += 1
        if not digit == c:
            return False
    return True


counter = 0
start_point = 10
correct_point = start_point
while correct_point < 987_654_321:
    correct_point = start_point
    if if_Pandigital_number(correct_point) and is_prime_num(correct_point):
        counter = correct_point
    start_point += 1
print('largest  Pandigital prime below 1,000,000', counter)
