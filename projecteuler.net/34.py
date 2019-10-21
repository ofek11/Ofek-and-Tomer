import math


def number_to_digits(number):
    str_number = str(number)
    digits = []
    for digit in str_number:
        digits.append(int(digit))
    return digits


def fact_of_digits(digits):
    c = 0
    for number in digits:
        c += math.factorial(number)
    return c


counter = 0
for num in range(3, 2540161):
    fact_number = fact_of_digits(number_to_digits(num))
    if fact_number == num:
        print(num)
        counter += num
print(counter)
