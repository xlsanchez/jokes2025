
# # # Luis Zuniga-Urzua, Xavier

# # #Knock-Knock Joke Program 
# # #List: storing the jokes 

# jokes1 = ['robbers', 'tanks', 'pencils']


# jokes = [
#     {"topic": "robbers", "who": "Calder", "punchline": "Calder police - I've been robbed!"},
#     {"topic": "tanks", "who": "Tank", "punchline": "You are welcome!"}, 
#     {"topic": "pencils", "who": "Broken pencil", "punchline": "Nevermind, it's pointless!"}
# ]

# #Abstraction 
# #Function --> tells the joke using parameters 
      




# #Function --> finds and tells selcted joke 
# def play_joke(choice):
#     for joke in jokes: #(Iteration)
#         if joke["topic"] == choice: #(selection)
#             tell_joke(joke["who"], joke["punchline"])
#         return 
#     else: 
#         jokes.append({ 
#             "topic": choice, 
#             "who": "New joke", 
#             "punchline": "This joke was just added!"
#         })
#         print("That joke didn't exist, so a new one was added.")
#         return
    
# joke = input("Do you want to hear a joke?")
# if joke == "no":
#     print("Okay bye!")

# #Iteration
# while joke == "yes":
#     print("Great, Let's play")
#     question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#     play_joke(question)
#     joke = input("Do you want to hear another joke or are you finished?")

# #Selection
# if joke == "finished":
#     rate = int(input("Please rate my jokes 1-10!"))
#     final_score = rate * 10 
#     print(str(final_score) + " percent satisfaction")

#     friend = input("Would you recommend to others?")

#     if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it!")
#     else: 
#         print("Sorry you didn't enjoy.")


# play_joke()


# Knock-Knock Joke Program

# Knock-Knock Joke Program

jokes = [
    {"topic": "robbers", "who": "Calder", "punchline": "Calder police - I've been robbed!"},
    {"topic": "tanks", "who": "Tank", "punchline": "You are welcome!"},
    {"topic": "pencils", "who": "Broken pencil", "punchline": "Nevermind, it's pointless!"}
]

# Function → tells the joke
def tell_joke(who, punchline):
    print("Knock knock.")
    print("Who's there?")
    print(who + ".")
    print(who + " who?")
    print(punchline)

# Function → finds and tells selected joke
def play_joke(choice):
    for joke in jokes:  # iteration
        if joke["topic"] == choice:  # selection
            tell_joke(joke["who"], joke["punchline"])
            return  # stop after telling the joke

    # If no joke found, add a new one
    jokes.append({
        "topic": choice,
        "who": "New joke",
        "punchline": "This joke was just added!"
    })
    print("That joke didn't exist, so a new one was added.")

# Program starts
joke = input("Do you want to hear a joke? ")

if joke == "no":
    print("Okay bye!")

while joke == "yes":
    print("Great, let's play!")
    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
    play_joke(question)
    joke = input("Do you want to hear another joke or are you finished? ")

if joke == "finished":
    rate = int(input("Please rate my jokes 1–10: "))
    final_score = rate * 10
    print(str(final_score) + "% satisfaction")

    friend = input("Would you recommend this to others? ")

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it!")
    else:
        print("Sorry you didn't enjoy.")



