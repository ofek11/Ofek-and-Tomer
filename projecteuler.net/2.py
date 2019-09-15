total = 0
x, y = 0, 1
while y < 4000000:
    x, y = y, x + y
    if x % 2:
         total += x

print (total)
