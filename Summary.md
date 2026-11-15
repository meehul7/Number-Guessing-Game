# Project Summary: Number Guessing Game

**PS No.:** 95

**Language:** Python 3

**Concepts:** Loops, Conditions, Functions, Random

**Code file:** `number_guessing_game.py`

---

## 1. Project Overview

This project is a console-based guessing game. The computer picks a secret number between 1 and 100, and the player has 5 attempts to guess it. After each guess, the game says `Too high!` or `Too low!`. When the game ends, it shows the attempts used and asks `Play again? (y/n)`. For testing, the secret number is fixed to 42.

## 2. What I Have Done

- Used `random.randint(1, 100)` to pick the secret number, and then fixed it to **42** for testing, as the project sheet says.
- Put one full game inside a function named `play_game()`, so it can be called again for "Play again".
- Used a **`while` loop** to control the 5 attempts, with a counter named `tries_used`.
- Used `if`, `elif` and `else` to give the `Too low!`, `Too high!` and `Congratulations!` messages.
- Added checks for wrong input. Letters like `abc` give `Invalid input. Enter a whole number.` and numbers like `150` give `Out of range. Enter a number between 1 and 100.`
- Made sure wrong input does **not** use up an attempt. The attempt is counted only after the input is found correct.
- Showed `Attempts left` after every guess, and `Attempts used` when the game is over.
- Added a `while True` loop at the end that asks `Play again? (y/n)` and stops when the answer is not `y`.
- Added a short comment on every line of the code, so it is easy to understand.
- Tested the program with all 4 given test cases.

## 3. Test Cases and Screenshots

### Test Case 1: Normal Input

**Input:** Secret number: 42, Guess: 42

**Expected output:** `Congratulations! You guessed it in 1 attempt.`

The guess matched the secret number on the first try, so the game ended with the win message. It then asked `Play again? (y/n)`, and `n` stopped the program.

<img width="1280" height="988" alt="Test Case 1" src="https://github.com/user-attachments/assets/84c1e7b6-0f22-4b64-bf9b-8adc40837af0" />


Output as text:

```text
Enter your guess (1-100): 42
Congratulations! You guessed it in 1 attempt.
Play again? (y/n): n
Thanks for playing!
```

### Test Case 2: Boundary / Minimum Input

**Input:** Secret number: 42, Guesses: 1, then 100 (range limits)

**Expected output:** `Too low! Attempts left: 4` and `Too high! Attempts left: 3`

Both limits of the range (1 and 100) were accepted as valid guesses. 1 is lower than 42 and 100 is higher than 42, so the hints were correct and the attempts left went down by one each time.

<img width="1028" height="808" alt="test case 2" src="https://github.com/user-attachments/assets/a5d37bbe-0857-4501-9dca-e99732b30000" />


Output as text:

```text
Enter your guess (1-100): 1
Too low! Attempts left: 4
Enter your guess (1-100): 100
Too high! Attempts left: 3
```

### Test Case 3: Invalid Input

**Input:** Secret number: 42, Guesses: abc, then 150

**Expected output:** `Invalid input. Enter a whole number.` and `Out of range. Enter a number between 1 and 100.` with `Attempts left: 5` (no attempt lost)

Both wrong inputs were rejected with the correct messages. The attempts left stayed at 5 each time, so no attempt was lost, and the program asked again without crashing.

<img width="1280" height="1103" alt="test case 3" src="https://github.com/user-attachments/assets/1ca98f2c-4ae5-4823-8a9b-788b0f4685af" />


Output as text:

```text
Enter your guess (1-100): abc
Invalid input. Enter a whole number.
Attempts left: 5
Enter your guess (1-100): 150
Out of range. Enter a number between 1 and 100.
Attempts left: 5
```

### Test Case 4: Different Valid Scenario

**Input:** Secret number: 42, Guesses: 10, 90, 50, 30, 20

**Expected output:** `Too low`, `Too high`, `Too high`, `Too low`, `Too low`, then `Game Over! The number was 42.`

All 5 guesses were wrong, so the attempts left went from 4 down to 0. After the last attempt, the game showed `Game Over!` with the secret number and the attempts used.

<img width="1020" height="1032" alt="test case 4" src="https://github.com/user-attachments/assets/6cf61456-cfbe-4833-bc79-6bf746e08703" />


Output as text:

```text
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

## 4. Hardships Faced and How I Overcame Them

| Hardship | How I Overcame It |
|---|---|
| **Understanding the test cases.** The "no attempt lost" rule in Test Case 3 was confusing at first. | I read the problem statement again and again, wrote the steps on paper, and then wrote the code step by step. |
| **Guess was text, not a number.** My comparison did not work because `input()` always gives text. | I changed the text into a number using `int()` before comparing it with the secret number. |
| **Program crashed on letters.** Typing `abc` stopped the program with a `ValueError`. | I check the input with `isdigit()` first. If it is not a whole number, the program prints `Invalid input` and asks again. |
| **Wrong input used up attempts.** Even `abc` or `150` reduced the attempts, but the test case says no attempt should be lost. | I used `continue` for wrong input, and I add 1 to `tries_used` only after the input is found correct. |
| **"Attempts left" was off by one.** It showed 5 left after the first valid guess. | I increase `tries_used` first and then print `5 - tries_used`. I checked the numbers with Test Case 2 (4 left, then 3 left). |
| **Random number made testing hard.** The secret number changed every time, so I could not match the expected output. | I fixed the secret number to 42 for testing and added a comment saying to remove that line for a real game. |
| **Messages not matching the sheet.** My output was close, but small differences like `attempt` and `attempts` did not match. | I compared each message with the expected output word by word. I also print `1 attempt` for one try and `attempts` for more. |
| **Indentation errors.** Python showed `IndentationError` because the spaces in my loops and `if` blocks were not equal. | I used 4 spaces every time and checked that each line was in the right block. |
| **Making "Play again?" work.** I did not know how to restart the game without copying the code. | I put the game inside the `play_game()` function and called it in a `while True` loop. The loop stops with `break` when the answer is not `y`. |

## 5. What I Learned

- How to repeat steps using a `while` loop.
- How to make decisions using `if`, `elif` and `else`.
- How to check the user's input so the program does not crash.
- How to keep code neat by putting the game in a function.
- How to pick a random number using the `random` module.
- How to test a program against given test cases and find the reason for a difference in output.

## 6. How to Run

```bash
python number_guessing_game.py
```

For testing, the secret number is fixed to 42. To play with a random number, remove the line `secret_number = 42` in the code.

## 7. Files in This Project

```
Python-Projects/
├── number_guessing_game.py   # main program
├── images/                   # screenshots of the 4 test cases
├── README.md                 # project description
└── Summary.md                # this summary
```
