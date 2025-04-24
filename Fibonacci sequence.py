#first 2 default numbers.
n1 = 0
n2 = 1

limit = int(input("Enter upper limit.--> "))
print(0)
n=1
while n <= limit:
    print(n)
    n = n1 + n2
    n1 = n2
    n2 = n