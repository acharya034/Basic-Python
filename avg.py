numbers = []

print("enter Some numbers and other then number to end.")
while True:
    try:
        num = float(input("> "))
    except: break
    if len(numbers)==0 : avg = 0
    numbers.append(num)
    avg = sum(numbers)/len(numbers)
    if int(avg)== avg: avg=int(avg)
print(avg)
    
    
