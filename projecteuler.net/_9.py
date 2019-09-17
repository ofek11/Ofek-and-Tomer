sum=1000
A=[]
for a in range(1,sum):
    b=a+1
    for b in range(1,sum-a):
        c=sum - a - b
        if a**2 + b**2 == c**2:
            print(a*b*c)
            break

