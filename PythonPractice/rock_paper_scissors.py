import random

ai_wins = 0
user_wins = 0
 
def get_random_choice():
    tools = ["Rock", "Paper", "Scissors"]
    return random.choice(tools)
while True:
    ai_input = get_random_choice()
    user_input = input("Fancy a game of rock, paper, scissors? : ")
    user_input = user_input.title()
    print(f"\nYou chose {user_input}, computer chose {ai_input}.")

    if user_input != "Rock" and user_input != "Paper" and user_input != "Scissors":
        print("Wrong answer, dummy!")
        break
    if user_input == ai_input:
        print(f"It's a tie! I also chose {ai_input}")
    elif user_input == "Rock":
        if ai_input == "Scissors":
            print("Rock smashes scissors! You win!")
            user_wins +=1
        else:
            print("Paper covers rock, you lose sucka!")
            ai_wins +=1
    elif user_input == "paper":
        if ai_input == "Rock":
            print("Paper covers rock! sick bro, high five!!!")
            user_wins +=1
        else:
            print("Scissors cuts paper! Now you die~")
            ai_wins +=1
    elif user_input == "scissors":
        if ai_input == "Paper":
            print("Scissors cuts paper! You win 1000000 dollars!")
            user_wins +=1
        else:
            print("Rock smashes scissors! I'm sorry, you lose.")
            ai_wins +=1
    print(f"Score:{user_wins} vs. {ai_wins}")
    print()

    if user_wins > ai_wins:
        print("Congrats you wont the game, you get a cookie!")
    elif user_wins < ai_wins:
        print("Too bad, you lose... and you will go to jail")
    else:
        print("GG bro, new game?")
       
    
    print(f"\nYou chose {user_input}, computer chose {ai_input}.")