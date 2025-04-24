import random, time, os

def clear():
    time.sleep(1)
    os.system("clr")

def tim(t):
    time.sleep(t)

    

# Add 100 more words to the list (this is just an example of random words)
name = [
    "apple", "banana", "grape", "orange", "kiwi", "mango", "peach", "plum", "pear", "cherry",
    "carrot", "potato", "cucumber", "lettuce", "tomato", "onion", "garlic", "spinach", "broccoli", "cabbage",
    "cat", "dog", "fish", "bird", "hamster", "rabbit", "turtle", "snake", "frog", "lizard",
    "book", "pen", "pencil", "notebook", "eraser", "sharpener", "ruler", "scissors", "paper", "glue",
    "table", "chair", "sofa", "bed", "desk", "lamp", "mirror", "carpet", "curtain", "picture",
    "mountain", "river", "lake", "ocean", "forest", "desert", "city", "village", "town", "street",
    "school", "university", "college", "library", "classroom", "teacher", "student", "bookstore", "cafeteria", "playground",
    "music", "guitar", "piano", "drums", "violin", "trumpet", "flute", "saxophone", "trombone", "keyboard",
    "sun", "moon", "star", "planet", "galaxy", "universe", "sky", "cloud", "rain", "snow",
    "applepie", "chocolate", "cake", "icecream", "cookie", "donut", "cupcake", "muffin", "pie", "tart",
    "sandwich", "burger", "pizza", "pasta", "sushi", "tacos", "salad", "soup", "steak", "grilledchicken",
    "ball", "bat", "soccer", "basketball", "tennis", "volleyball", "swimming", "cycling", "running", "hiking",
    "snowboarding", "skiing", "surfing", "skateboarding", "boxing", "martialarts", "fencing", "golf", "rugby", "baseball"
]



while True:
    clear()
    p = {}
    na = ""
    q = set()
    live = 5

    def life(a):
        global live
        return " ".join(["🤍"] * live)


    print("Hey there today we are going to play hanging game.")
    print("Guess the character and combine to form a word.")

    Name = random.choice(name)

    for i in range(len(Name)):
        j = random.randint(0,10)
        k = Name[i] 
        if j % 4 == 0 :

            na += k
        else:

            p[i] = Name[i]
            q.add(i)
            na += "_"

    # print(p)
    while True:
        print("Your life is ",life(0))
        print(na)
        print("Guess the missing letter ")
        char = input(">> ")
        found = False
        for ind in list(q):
            # ind = str(ind)
            if p[ind] == char.lower():

                print("Yes keep it up.")
                q.remove(ind)
                found = True
                # del p[]

        if not found:
            print("Try once again.")
            live -=1
        
        else:
            for i in range(len(Name)):
                if Name[i] == char:
                    na = na[:i] + char + na[i + 1:]
        
        if not  q:
            print("you have find word ",Name)
            break
        if live == 0:
            print("you have reach your limit.")
            break
    yes = input("Do you want to play again.\n >> ").strip().lower()
    if yes[0] == "n":
        break