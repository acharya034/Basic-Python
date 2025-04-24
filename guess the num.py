import random
print("Hey their life is way of enjoy. \n Today, lets play a game.")
rand = random.randint(1,9)
print("Guess a number between 1 to 10. \n You have 3 chance, I will guide your guess, if you able to guess you win.")
game_life = 3
def res():
    print("the actual num is ",rand)
while game_life > 0:
    in_rand = int(input("Enter a number: "))
    
    
    if in_rand == rand :
        print("wow you win😀!")

    elif in_rand >= 10 :
        print("not more than 10!")
    elif in_rand <= rand :
        print("Your guess is lesser then that")
       # print("your life is "life[game_life])
        game_life -= 1
    elif in_rand >= rand :
        print("Your guess is greater then that")
        game_life -= 1
    if game_life == 0:
        print(res())
    elif game_life == 2:
        print("❤❤")
    elif game_life == 1:
        print("❤")
