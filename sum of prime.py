def prime(n):
    status = True
    i = 2
    if n < 2:
        status = False
    while i < n:
        if n % i == 0:
            status = False
            break
        i +=1
    if status == True:
        return 1


sum = 0
for num in range(100):
    if prime(num):
        sum += num

print("sum of prime is ",sum)