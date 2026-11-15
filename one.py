# Number Guessing Game
# The computer thinks of a number from 1 to 100 and I have 5 tries to find it.

import random  # bring in the random tool to pick a random number


def play_game():  # one function that plays one full game
    # The computer picks a secret number
    secret_number = random.randint(1, 100)  # pick a random number from 1 to 100

    # For testing the number is always 42.
    # Remove this line to get a different number every time.
    secret_number = 42  # fix the number to 42 for testing

    tries_used = 0  # no tries used at the start

    # Keep asking until all 5 tries are used
    while tries_used < 5:  # repeat while tries are less than 5
        answer = input("Enter your guess (1-100): ")  # ask the player for a guess (text)

        # If it's not a whole number, ask again (no try is lost)
        if not answer.isdigit():  # check if the answer is not a whole number
            print("Invalid input. Enter a whole number.")  # show error message
            print("Attempts left:", 5 - tries_used)  # show tries left (no try lost)
            continue  # go back and ask again

        guess = int(answer)  # change the text into a number


        # If it's outside 1-100, ask again (no try is lost)
        if guess < 1 or guess > 100:  # check if the number is out of range
            print("Out of range. Enter a number between 1 and 100.")  # show error message
            print("Attempts left:", 5 - tries_used)  # show tries left (no try lost)
            continue  # go back and ask again


