# import library
import random  

# Declare variables
player = {}  # Player name
name = []  # Name list
characterlist = ["raja", "rani", "police", "chor"]
tempchar = {}
j = 1

# Welcome message
print("Hello world, let's play Raja Rani today.")
print("In this game, all players are assigned roles as in a kingdom. One of you is the police and must find the 'chor' (thief).")
print("\tIf the police can't find the chor, 50% of the police's points go to the chor, and the police quit the game. If the police catches the chor, the chor is eliminated.")

# Number of players
plaNum = int(input("How many players are there?\n>> "))
print("Name yourself and your friends individually.")

# Insufficient players
if plaNum < 4:
    print("O! I think you don't have enough friends. To play this awesome game, you need at least 4 players.")
else:
    # Save player names
    for i in range(plaNum):
        print(f"Player {i + 1}: ", end="")
        playerName = input("\b >> ")
        player[i + 1] = playerName
        name.append(playerName)

# Function to print names excluding the given name
def printname(exclude):
    print("Remaining players:")
    for idx, player_name in enumerate(name, start=1):
        if player_name != exclude:
            print(f"{idx}: {player_name}")

# Function to randomly assign roles
def rand():
    global j
    if not characterlist and j > 4:
        return None  # All roles exhausted
    randomplayer = random.choice(name)
    name.remove(randomplayer)
    if j <= 4:
        character = random.choice(characterlist)
        characterlist.remove(character)
        j += 1
    else:
        character = "mantri"
    tempchar[randomplayer] = character
    return [randomplayer, character]

# Function to select the police
def police():
    while True:
        randomResult = rand()
        if randomResult and randomResult[1] == "police":
            return randomResult[0]
        
# Game loop
while True:
    Police = police()
    if Police:
        print(f"\nHey {Police}, you have been selected as the police! Guess who the chor is.")
        printname(Police)
    else:
        print("All roles have been assigned. Game over!")
        break