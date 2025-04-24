# need to have same character on first and last of both.

feast = input("whats your name? \n\t->").lower().strip()
beast = input("what you want to eat? \n\t->").lower().strip()
if feast[0] == beast[0] and feast[-1] == beast[-1]:
    print("Okay move on.")
else:
    print("choose other.")
