list = []
print("Enter some non zero numbers and 0 to end.")
while True:
    i = float(input("> "))
    if int(i)==i:i=int(i)
    if i == 0: break
    list.append(i)
    print(list)
pro =1
if list == []: pro=0
for i in list:pro*=i
print("the product of your number is ",pro)
