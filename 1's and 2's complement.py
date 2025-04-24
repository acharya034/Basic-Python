import time,os
# print("\n"*5)
# Define ANSI color codes
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = '\033[34m'
reset = "\033[0m"  # Reset to default color

# Clear all screen first.
os.system('cls')

# temp number for testing
# min = "11100"
# sub =  "1011"
# method = "2's"
# method = "1's"

# time
def tim():
    time.sleep(.1)
# for 1's complement..
def com(sub):
    sub1 = ""
    for i in range(len(sub)):
        if sub[i] == "1":
            l="0"
        elif sub[i] == "0" :
            l="1"
        sub1 = sub1 + l
    return sub1

tim()
print(blue,"This is a subtracting program by 1's and 2's method.",reset)
min = input("Enter minued.\n\t>> ")
sub = input("Enter subtrahend.\n\t>> ")
method = input("By which method you want to use.(1's or 2's)")



if method[0] == "1":
    tim()
    print(red,"By 1's complements method.")
    # chick the num of digit if its not equal make it...
    tim()
    print(green,"\nMake the number of digit equal on both side by adding 0 at leftmost of the least number of digit.")
    if len(min) > len(sub):
        j = len(min) - len(sub)
        i = "0"*j
        k = sub
        sub = i + sub
        print(reset,"In this case that is subtrahend so ", k , " become ", sub)
    elif len(sub) > len(min):
        j = len(sub) - len(min)
        i = "0"*j
        k = min
        min = i + min
        print(reset,"In this case that is minuend so ", k , " become ", min)
    tim()
    sub1 = com(sub)
    print(green,"\nCalculate 1's complement of subtrahend.")
    print(reset,"First complement of ",sub ," is ",sub1)

    tim()
    # to sum two values
    print(green,"Sum of minuend and 1's complement of subtrahend.",reset)
    print("\t ",min,"\n      +\t ",sub1)
    sum = bin(int(min, 2) + int(sub1, 2))
    sum = str(sum[2:])
    print("      =\t",sum)

    tim()
    # Chicking Overflow of sum.
    if len(sum) > len(min):
        print(yellow,"Here the sum has one overflow so remove it and add on remaining number.",reset)
        sum = sum[1:]
        sum1 = bin(int(sum,2) + int("1",2))
        sum1 = sum1[2:]
        print("Add 1 on it, ",sum," + 1 = ",sum1)

    else:
        print(yellow,"Here is no overflow so the result is negative so find 1's complement of sum and add negative sign.",reset)
        if len(sum) < len(min):
            sum = str(sum)
            sum = "0"+sum
        sum1 = com(sum)
        print("1's complement of ",sum," is ",sum1)
        i = "-"
        sum1 = i + sum1
        print("Add - sign.")
        # to print result.
    print(f"{red}Thus the result is ({sum1})\u2082")



# for 2's complement.....
elif method[0] == "2":
    tim()
    print(red,"By 2's complements method.")
    # chick the num of digit if its not equal make it...
    tim()
    print(green,"\nMake the number of digit equal on both side by adding 0 at leftmost of the least number of digit.")
    if len(min) > len(sub):
        j = len(min) - len(sub)
        i = "0"*j
        k = sub
        sub = i + sub
        print(reset,"In this case that is subtrahend so ", k , " become ", sub)
    elif len(sub) > len(min):
        j = len(sub) - len(min)
        i = "0"*j
        k = min
        min = i + min
        print(reset,"In this case that is minuend so ", k , " become ", min)
    tim()
    sub1 = com(sub)
    print(green,"\nCalculate 2's complement of subtrahend.")
    print("For this convert to 1's complement first and add 1 on it.")
    print(reset,"1's complement of ",sub," is ",sub1)
    # i = "1"
    sub2 = bin(int(sub1,2) + int("1",2))
    print("2's complement is ",sub1," + 1 =",sub2)

    tim()
    # to sum two values
    print(green,"Sum of minuend and 2's complement of subtrahend.",reset)
    print("\t ",min,"\n      +\t ",sub2[2:])
    sum = bin(int(min, 2) + int(sub2, 2))
    sum = str(sum[2:])
    print("      =\t",sum)

    tim()
    # Chicking Overflow of sum.
    if len(sum) > len(min):
        print(yellow,"Here the sum has one overflow so remove it and the remaining number is result.")
        sum = sum[1:]
        print(red,"Thus, the result is (",sum,")\u2082",reset)

    else:
        print(yellow,"Here is no overflow so the result most be negative so convert it to 2's complement add 1 on the 2's complement and negative sign as welll.",reset)
        i = "1"
        sum = str(sum)
        sum1 = com(sum)
        if int(sum1) == 0:
            sum1 = i + str(sum1)
        sum2 = bin(int(sum1,2) + int(i,2))
        sum2 = sum2[2:]
        print("2's complement of ",sum," is ",sum1," and ",sum1," + 1 = ",sum2)

        i = "-"
        sum2 = i + sum2
        print("Add - sign ",sum2)
        print(f"{red}Thus, the result is ({sum2})\u2082")


