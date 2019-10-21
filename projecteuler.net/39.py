l = []
for a in range(1, 500):
    for b in range(a, 500):
        c = (a**2 + b**2)**0.5
        if int(c) == c and a + b + c <= 1000:
            l.append([a, b, int(c)])
print(l)