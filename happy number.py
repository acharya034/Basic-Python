# Happy number if sum of square of digits of that number is equal to that number.
# try 19, 68...
print("Hello, Are you guessing a happy number. I can tell you.")
num = int(input("Enter your number here.--> "))

for i in range(100):
    sum = 0
    Snum = str(num)
    for j in range(len(Snum)):
        sum += int(Snum[j])**2
    if sum == 1:
        print("Yes, its a happy number.")
        break
    num = sum
if sum != 1:
    print("No its a unhappy number. try again.")
