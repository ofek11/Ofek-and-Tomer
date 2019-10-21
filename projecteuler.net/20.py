import math

number = str(math.factorial(100))
Sum_Of_Digit = 0
for i in number:
    Sum_Of_Digit += int(i)
print(Sum_Of_Digit)
