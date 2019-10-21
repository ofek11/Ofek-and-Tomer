from functools import lru_cache


@lru_cache(maxsize=10000)
def Fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


valid = True
number = 0
while valid:
    number += 1
    if 10 > Fibonacci(number) / 10 ** 999 > 1:
        valid = False
print(number)
