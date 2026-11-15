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