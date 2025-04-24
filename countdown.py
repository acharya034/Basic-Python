import time, os
print("Count down for you")
print("Enter time.")
hr = int(input("Enter Hour: "))
min = int(input("Enter Minute: "))
sec = int(input("Enter Second: "))
while sec > 0:
    time.sleep(1)
    os.system("cls")
    sec -= 1
    if hr != 0:
        print("hour",hr) 
    if min != 0:
        print("minutes",min) 
    if sec != 0:
        print("second",sec) 
    if sec == 0 and min != 0:
        sec = 60
        min -= 1
        if min == 0 and hr != 0:
            min = 60
            hr -= 1
print("Time up ..")