def is_prime_num(num):
    import math
    i=1
    for i in range(1,int(math.sqrt(num+1))):
        i+=1
        if num%i==0:
            return False
    return True
counter=0
number=0
while counter != 10_001:
    number+=1
    if is_prime_num(number)==True:
        counter+=1
    print(counter)
print('end',number)