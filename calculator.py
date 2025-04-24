print("select the sembol to run operation respect to its num.")
while 1>0:
    opera = int(input("1. + \n 2. - \n 3. X \n 4. / \n 5. power \n 6. moduos \n 7. root"))

    a = int(input("enter first num:"))
    b = int(input("enter second num:"))
    if opera == 1 :
        c = a + b
    elif opera == 2:
        c = a - b
    elif opera == 3:
        c = a * b
    elif opera == 4:
        c = a / b
    elif opera == 5:
        c = a ** b
    elif opera == 6:
        c = a % b
    elif opera == 7:
        c = a ** (1/b)
    print("the result is ",c)


