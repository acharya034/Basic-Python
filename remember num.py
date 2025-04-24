import time , random, os
co = 0
os.system('cls')
yes = 0
while yes != 1:
    co += 1
    list = []
    for i in range(co):
        os.system('cls')
        print("Remember given number, and enter one by one in same patten")
        ran = random.randint(0,9)
        list.append(ran)
        print(ran)
        time.sleep(1)
    j = 0
    os.system('cls')
    while j < co:
        num = int(input("enter>> "))
        if num != list[j]:
            yes = 1
            print("sorry, you got wrong; the correct patton is ")
            for i in list:
                print(i)
            break
        j += 1
    if j == co:
        print("Congratulations! You remembered the pattern correctly! \n now move to next lev1el ",co+1)
        time.sleep(1)
        

    