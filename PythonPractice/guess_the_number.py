import random
secret_number = random.randint(1,100)
number_of_guesses = 0
# Keep a counter for guesses
def computer_number():
    return random.randint(1,100)
while True:
    user_input = int(input("Guess what number I'm thinking... "))
    if user_input < secret_number:
        print("Too low!")
        number_of_guesses +=1
    if user_input > secret_number:
        print("Too high!")
        number_of_guesses +=1
    if user_input == secret_number:
        print(f"Wow! You did it with {number_of_guesses} guesses!")
        break



    # Read human input
    # Check if the input is High or Low (compare it with secret_number)
    # If the number given is the secret_number break out!