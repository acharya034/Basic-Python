import random
print("Hey their, can you beat me on seasor paper rock.")
print("If yes, we are going to play 10 and if you win more then 5 times then you win.")
print("Type s for 'scissor', p for 'paper' and r for 'rock'")
list = ["r", "p" ,"s"]
user_sc = 0
com_sc = 0
com_move_num = int(random.randint(0,len(list)-1))
count = 10
while count > 0:
    com_move = list[com_move_num]
    user_move = str(input("Enter your move.\n>>> "))
    if com_move == "s" :
        if user_move == "s":
            print("We both have same choice. Both got a point!")
            user_sc += 5
            com_sc += 5
            count += 1
            com_move_num = int(random.randint(0,len(list)-1))
        elif user_move == "r":
            print("You beat me this time.You got a point!")
            user_sc += 5
            com_move_num += 1
            if com_move_num == 3:
                com_move_num = 0
        elif user_move == "p":
            print("I beat You this time. I got a point!")
            com_sc += 5
            com_move_num -= 1
            if com_move_num == -1:
                com_move_num = 2
    elif com_move == "p" :
        if user_move == "p":
            print("We both have same choice. Both got a point!")
            user_sc += 5
            com_sc += 5
            count += 1
            com_move_num = int(random.randint(0,len(list)-1))
        elif user_move == "s":
            print("You beat me this time.You got a point!")
            user_sc += 5
            com_move_num += 1
            if com_move_num == 3:
                com_move_num = 0
        elif user_move == "r":
            print("I beat You this time. I got a point!")
            com_sc += 5
            com_move_num -= 1
            if com_move_num == -1:
                com_move_num = 2
    elif com_move == "r" :
        if user_move == "r":
            print("We both have same choice. Both got a point!")
            user_sc += 5
            com_sc += 5
            count += 1
            com_move_num = int(random.randint(0,len(list)-1))
        elif user_move == "p":
            print("You beat me this time.You got a point!")
            user_sc += 5
            com_move_num += 1
            if com_move_num == 3:
                com_move_num = 0
        elif user_move == "s":
            print("I beat You this time. I got a point!")
            com_sc += 5
            com_move_num -= 1
            if com_move_num == -1:
                com_move_num = 2
    count -= 1
print(f"Oh! you got {user_sc} points. \n \t AND \n I got {com_sc} points.")
if user_sc > com_sc :
    print("\n \t You are the winner.")
elif user_sc < com_sc :
    print("\n \t I am the winner.")
else:
    print("Both got same score.")

