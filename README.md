# Number Guessing Game

A console-based guessing game written in Python 3. The computer picks a secret number between 1 and 100, and the player has 5 attempts to guess it. After each guess, the game says "Too high" or "Too low". At the end, it asks if the player wants to play again.

**PS No.:** 95
**University:** Rungta International Skills University 
**School:** School Of Computer Science And Engineering 
**Course:** B.Tech CSE Core
**Language:** Python 3
**Concepts:** Loops, Conditions, Functions, Random

---

## Problem Statement

Create a game in which the computer picks a random number between 1 and 100 and the player guesses it within limited attempts, receiving "Too high" or "Too low" hints. The player gets 5 attempts. For testing, the secret number is fixed to 42.

## Features

- The computer picks a random secret number between 1 and 100
- The player gets 5 attempts
- Hints after every guess: "Too high" or "Too low"
- Shows the attempts left after every guess
- Checks the input: only whole numbers from 1 to 100 are accepted
- Wrong input does not use up an attempt
- Shows a win message with the number of attempts used
- Shows "Game Over" with the secret number when all attempts are used
- Asks "Play again? (y/n)" at the end

## How the Program Works

1. The program calls `play_game()`, which picks the secret number using `random.randint(1, 100)`. For testing, the number is then fixed to 42.
2. A `while` loop runs until the player has used 5 attempts.
3. The player types a guess. If it is not a whole number, or it is outside 1 to 100, an error message is shown and the player is asked again. No attempt is lost.
4. If the guess is valid, `tries_used` goes up by 1.
5. The guess is compared with the secret number:
   - If it is equal, the win message is shown and the game ends.
   - If it is smaller, `Too low!` is shown with the attempts left.
   - If it is bigger, `Too high!` is shown with the attempts left.
6. If all 5 attempts are used without a win, `Game Over!` is shown with the secret number and the attempts used.
7. The program asks `Play again? (y/n)`. If the answer is `y`, a new game starts. Otherwise, the program stops.

## Variables Used

| Variable | What it stores |
|---|---|
| `secret_number` | The number the computer picked (fixed to 42 for testing) |
| `tries_used` | How many valid guesses the player has used (starts at 0) |
| `answer` | What the player typed, as text |
| `guess` | The player's answer changed into a whole number |
| `play_again` | The player's answer to "Play again? (y/n)" |

## Functions

| Function | What it does |
|---|---|
| `play_game()` | Plays one full game: picks the number, takes the guesses, checks the input, gives the hints and shows the result |

The main program runs `play_game()` inside a `while True` loop, so the game can be played again.

## Rules and Validation

- The guess must be a whole number. Letters, decimals and negative signs show `Invalid input. Enter a whole number.`
- The guess must be from 1 to 100. Other numbers show `Out of range. Enter a number between 1 and 100.`
- Wrong input does not use up an attempt.
- The player gets exactly 5 valid attempts.
- Any answer other than `y` (in small or capital letters) to "Play again?" ends the program.

## Requirements

- Python 3.x
- No external libraries are needed (only the built-in `random` module is used)

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the program:

```bash
python one.py
```

4. Type your guess when the program asks for it.

**Note:** For testing, the secret number is fixed to 42. To play with a random number, remove the line `secret_number = 42` in the code.

## Test Cases

| Test Case | Input | Expected Output |
|---|---|---|
| 1. Normal input | Secret number: 42, Guess: 42 | `Congratulations! You guessed it in 1 attempt.` |
| 2. Boundary input | Secret number: 42, Guesses: 1, then 100 | `Too low! Attempts left: 4` and `Too high! Attempts left: 3` |
| 3. Invalid input | Secret number: 42, Guesses: abc, then 150 | `Invalid input. Enter a whole number.`, `Out of range. Enter a number between 1 and 100.` and `Attempts left: 5` (no attempt lost) |
| 4. Different valid scenario | Secret number: 42, Guesses: 10, 90, 50, 30, 20 | `Too low`, `Too high`, `Too high`, `Too low`, `Too low`, then `Game Over! The number was 42` |

## Sample Run

```
Enter your guess (1-100): 10
Too low! Attempts left: 4
Enter your guess (1-100): 90
Too high! Attempts left: 3
Enter your guess (1-100): 50
Too high! Attempts left: 2
Enter your guess (1-100): 30
Too low! Attempts left: 1
Enter your guess (1-100): 20
Too low! Attempts left: 0
Game Over! The number was 42
Attempts used: 5
Play again? (y/n): n
Thanks for playing!
```

## Project Structure

```
Number-Guessing-Game/
├── number_guessing_game.py   # main program
├── images/                   # screenshots of the test cases
├── README.md                 # project description
└── Summary.md                # project summary
```

## Author

- Name: Mehul
- ERP: RU-26-01503
- Section: M
