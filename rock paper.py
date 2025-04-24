print("Rock,Paper,Scissors")
print()
print("Answer in 'r' for Rock, 'P' for Paper & 'S' for scissors")

player1 = input("player1 name:")
player2 = input("player2 name:")
print(player1, "and", player2, "Get ready for Battle")
p1 = input(player1,"Select your move (r, p or s)")
p2 = input(player2,"Select your move (r, p or s)")
exit = "no"
print()
while exit == "no":
    if p1 =="r":
    if p2 =="r":
        print("Draw!")
    elif p2 =="p":
        print(player1 ,"is winner")
    elif p2 =="s":
        print(player2 ,"is winner")

    elif p1 =="s":
    if p2 =="s":
        print("Draw!")
    elif p2 =="p":
        print(player1 ,"is winner")
    elif p2 =="r":
        print(player2 ,"is winner")

    elif p1 =="p":
    if p2 =="p":
        print("Draw!")
    elif p2 =="r":
        print(player1 ,"is winner")
    elif p2 =="s":
        print(player2 ,"is winner")

    else:
    print("Please answer in (r, p or s)")

    exit = input("do you want to quite:")