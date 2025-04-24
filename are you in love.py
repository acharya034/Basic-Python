print("\033[91m This project is made purely for entertainment purposes. The love calculation is based on a simple number parity rule and does not reflect real emotions, relationships, or compatibility. Please don't take the result seriously—just enjoy it and have fun! \033[0m ")

def love(a,b):
    return (a%2==0 and b%2==1) or (b%2==0 and a%2==1)

try:
    a = int(input("Whats your number of petals. "))
    b = int(input("Whats partner number of petals. "))
    if a<0 or b<0 :
        print("Enter positive one.")
    else:
        if love(a,b):
            print("Yes, You and your partner are in love.")
        else:
            print("No, Sorry try with other.")
except:
    print("please enter valid value.")