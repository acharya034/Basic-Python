import time
multiple = int(input("which multiple table you want?\n "))
long = int(input("How long table you want?\n  "))
# multiple = 3
# long = 4
t = .1
for i in range(long):
    result = f"{multiple} X {i+1} = {multiple*(i+1)}"
    for char in result:
        print(char,end = "", flush = True)
        time.sleep(t)
    print()
    t = t - t*1/100
