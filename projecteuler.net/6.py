sum=0
sum_2=0
for i in range(101):
    sum+=i**2
    sum_2+=i
sum_2= sum_2**2
final=sum_2-sum
print(final)
