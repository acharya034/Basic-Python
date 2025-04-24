import random, string
num = int(input("how many password you want? "))
re = "n"
if num != 1:
    length = int(input("how long password you want? \n >>"))
    re = input("you want same length password again? y/n")
while True:
    if re != "y":
        length = int(input("how long password you want? \n >>"))
    password = ""
    char = string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
        j = random.choice(char)
        password += j


    print("your password is ", password)
    num -= 1
    if num == 0 : break