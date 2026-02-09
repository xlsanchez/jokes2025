#Xavier Sandoval 
# Knock-Knock Joke Program


# LIST OF JOKES (Data Storage)

# Each joke is stored as a dictionary with:
# - topic: what the joke is about
# - who: the "who's there?" response
# - punchline: the final line of the joke
# All jokes are kept inside a list.
jokes = [
    {"topic": "robbers", "who": "Calder", "punchline": "Calder police - I've been robbed!"},
    {"topic": "tanks", "who": "Tank", "punchline": "You are welcome!"},
    {"topic": "pencils", "who": "Broken pencil", "punchline": "Nevermind, it's pointless!"}
]


# FUNCTION: tell_joke()

# This function prints a full knock‑knock joke.
# It uses parameters (who, punchline) so it can
# tell ANY joke without rewriting code.
# This is an example of ABSTRACTION.
def tell_joke(who, punchline):
    print("Knock knock.")
    print("Who's there?")
    print(who + ".")
    print(who + " who?")
    print(punchline)



# FUNCTION: play_joke()

# Purpose: Find the joke the user asked for.
# Uses:
# - ITERATION (loop through all jokes)
# - SELECTION (check if topics match)
# - ABSTRACTION (calls tell_joke)
#
# If the joke exists → tell it.
# If not → add a new joke to the list.
def play_joke(choice):
    for joke in jokes:  # ITERATION: loop through each joke
        if joke["topic"] == choice:  # SELECTION: check for match
            tell_joke(joke["who"], joke["punchline"])
            return  # stop after telling the joke
    else:
        # This else runs ONLY if the loop finds no match
        print("That joke didn't exist, so a new one was added.")
        jokes.append({
            "topic": choice,
            "who": "New joke",
            "punchline": "This joke was just added!"
        })
        return



# PROGRAM START

# Ask the user if they want to hear a joke.
joke = input("Do you want to hear a joke? ")


# FIRST DECISION

# If the user says no, the program ends.
if joke == "no":
    print("Okay bye!")



# MAIN LOOP

# As long as the user types "yes", the program repeats.
while joke == "yes":
    print("Great, let's play!")
    
    # Ask which joke topic they want
    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
    
    # Call the function to tell the joke
    play_joke(question)
    
    # Ask if they want another joke
    joke = input("Do you want to hear another joke or are you finished? ")



# ENDING + RATING SYSTEM

# If the user types "finished", the program ends politely.
if joke == "finished":
    rate = int(input("Please rate my jokes 1–10: "))
    
    # Simple math to turn rating into a percentage
    final_score = rate * 10
    print(str(final_score) + "% satisfaction")

    # Ask if they'd recommend the program
    friend = input("Would you recommend this to others? ")

    # Final message based on their answer
    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it!")
    else:
        print("Sorry you didn't enjoy.")



