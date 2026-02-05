
# Luis Zuniga-Urzua, Xavier

#Knock-Knock Joke Program 
#List: storing the jokes 
jokes = [
    {"topic": "robbers", "who": "Calder", "punchline": "Calder police - I've been robbed!"},
    {"topic": "tanks", "who": "Tank", "punchline": "You are welcome!"}, 
    {"topic": "pencils", "who": "Broken pencil", "punchline": "Nevermind, it's pointless!"}
]

#Abstraction 
#Function --> tells the joke using parameters 
def tell_joke(who, punchline):
    input("Knock Knock")
    input(who)
    input(punchline)

#Function --> finds and tells selcted joke 
def play_joke(choice):
    for joke in jokes: #(Iteration)
        if joke["topic"] == choice: #(selection)
            tell_joke(joke["who"], joke["punchline"])
        return 
    else: 
        jokes.append({ 
            "topic": choice, 
            "who": "New joke", 
            "punchline": "This joke was just added!"
        })
        print("That joke didn't exist, so a new one was added.")
        return
    
joke = input("Do you want to hear a joke?")
if joke == "no":
    print("Okay bye!")

#Iteration
while joke == "yes":
    print("Great, Let's play")
    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
    play_joke(question)
    joke = input("Do you want to hear another joke or are you finished?")

#Selection
if joke == "finished":
    rate = int(input("Please rate my jokes 1-10!"))
    final_score = rate * 10 
    print(str(final_score) + " percent satisfaction")

    friend = input("Would you recommend to others?")

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it!")
    else: 
        print("Sorry you didn't enjoy.")


