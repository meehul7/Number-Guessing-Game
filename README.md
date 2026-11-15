# Number Guessing Game

A simple Python console game where the computer picks a number between 1 and 100, and the player has five chances to guess it correctly. After each guess, the game gives feedback such as "Too low!" or "Too high!" and tracks how many attempts remain.

## Features

- Random secret number generation between 1 and 100
- Five-attempt gameplay loop
- Feedback for higher or lower guesses
- Validation for invalid input and out-of-range values
- Replay option after each round
- Beginner-friendly Python implementation

## Project Files

- `one.py` - main game logic
- `Summary.md` - project summary and testing notes
- `README.md` - project description and usage instructions

## How to Run

```bash
python one.py
```

If your system uses Python 3 explicitly, you can run:

```bash
python3 one.py
```

## How It Works

1. The game generates a secret number.
2. The player enters a guess between 1 and 100.
3. The program checks whether the guess is valid.
4. If the guess is correct, the player wins.
5. If not, the game provides a hint and continues until the player runs out of attempts.
6. After the round ends, the player can choose to play again.

## Example Gameplay

```text
Enter your guess (1-100): 42
Congratulations! You guessed it in 1 attempt.
Play again? (y/n): n
Thanks for playing!
```

## Note

The current version of the script includes a test value (`secret_number = 42`) so it is easier to verify the game logic during development. To make the game use a random number each round, remove that line in `one.py`.

## License

This project is provided for learning and personal use.
