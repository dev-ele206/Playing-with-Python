import random

with open("words.txt") as my_file:
    lines = my_file.readlines() # Read all lines from my_file
    secret_word = random.choice(lines)

    # The secret word now has a \n char at the end, remove it using a string method.
    secret_word = secret_word.rstrip("\n").lower() # here remove the \n

# Print the initial output of the word (first letter and remaining with _)
for index, char in enumerate(secret_word):
    if index == 0:
        print(f" {char.upper()}", end="")
    else:
        print(" _", end="")
print()

correct_letters = ""
wrong_inputs = 0
threshold = 5
# (1) You need to use a way to keep all the letters given by the user.
# You need a counter to keep record of the wrong inputs.

while True:
    user_input = input("Please provide a letter or the solution: ")
    if len(user_input) > 1:# Check if the given input is not a single char, if is > 1 char then is a solution
        if user_input.lower() != secret_word.lower(): # Check if the solution is correct.
            print(f"Game over, the secret word is {secret_word}")
            break
        else:
            print(f"You got it right! The secret word is {secret_word}")
            break
    elif len(user_input) == 1:
        if user_input in secret_word:
            print(f"The {user_input} is in the word!")
            correct_letters = correct_letters + user_input # Check if the given input is a single char.
        # Check if the letter appears in the secret word
            # Save that char in (1)
        else:
            wrong_inputs +=1
            print(f"Sorry, {user_input} is not in the word.") # Wrong input, increment wrong counter
    
    if wrong_inputs >= threshold:# check if the wrong counter is beyond the threshold
        print(f"Game over, you've reached {threshold} guesses.")
        break

    # Print again the word concealing the letter required and revealing the ones that the user guessed correctly (including the first letter)
    for index, char in enumerate(secret_word):
        if index == 0:
            print(f"{char.upper()}", end = "")
        elif char in correct_letters:
            print(f"{char}", end = "")
        else:
            print(" _", end = "")
        print()