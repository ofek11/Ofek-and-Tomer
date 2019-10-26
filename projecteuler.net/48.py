result = 0
for number in range(1, 1001):
    result += number ** number
result = str(result)
print(result[-10:])
