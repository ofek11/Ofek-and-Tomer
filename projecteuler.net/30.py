s, c, i = 0, 0, 10
sd = 0
for i in range(2, 10**6):
    j = list(str(i))
    for x in j:
        sd += int(x) ** 5
    if sd == i:
        s += i
    sd = 0
    i += 1
print(i)
print(s)