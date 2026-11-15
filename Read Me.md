# Number Guessing Game

## About My Project
This is a small game I made in Python. The computer thinks of a number from 1 to 100. I have 5 tries to guess it. The game tells me if my guess is too high or too low. At the end, it asks if I want to play again.

## How to Run
1. Install Python 3.
2. Open the terminal in the folder of the file.
3. Type this and press Enter:
   ```
   python number_guessing_game.py
   ```

Note: For testing, the secret number is always 42. To play with a random number, remove the line `secret_number = 42`.

---

## Problems I Faced and How I Fixed Them

### 1. I did not understand the test cases
At first, I did not understand what the 4 test cases wanted. The "no attempt lost" part was confusing.
**What I did:** I read the problem again and again. I wrote the steps on paper first, and then I wrote the code step by step.

### 2. Python did not treat my guess as a number
When I typed a guess, the comparison did not work. I found out that `input()` gives text, not a number.
**What I did:** I changed the text into a number using `int()`.

### 3. The program stopped when I typed letters
When I typed "abc", the program crashed with an error.
**What I did:** I used `isdigit()` to check the input first. Now it shows "Invalid input" and asks again.

### 4. Wrong input was using up my tries
At first, even "abc" or 150 used one try. But the test case says no try should be lost.
**What I did:** I used `continue` for wrong input. I count a try only after the input is checked and found correct.

### 5. "Attempts left" was showing the wrong number
The number was off by one.
**What I did:** I add 1 to the tries used first, and then I show `5 - tries_used`. I checked it with Test Case 2 (4 left, then 3 left).

### 6. The secret number kept changing
Because the number was random, I could not match the expected output.
**What I did:** I fixed the number to 42 while testing.

### 7. My messages were a little different
My output was almost right, but not exactly the same as the project sheet. For example, "attempt" and "attempts".
**What I did:** I compared my output with the sheet word by word and fixed it.

### 8. Indentation errors
Python showed `IndentationError` many times because my spaces were not equal.
**What I did:** I used 4 spaces every time and checked that every line was in the right place.

### 9. Making "Play again?" work
I did not know how to start the game again without copying the code.
**What I did:** I put the game inside a function. Then I called it inside a `while True` loop. If I type anything other than "y", the loop stops.

---

## Testing
I tested all 4 test cases from the project sheet.
- **Test 1:** I guess 42 and win in 1 attempt.
- **Test 2:** I guess 1 and 100. I get "Too low" and "Too high".
- **Test 3:** I type "abc" and 150. I get error messages and keep all 5 tries.
- **Test 4:** I guess 5 wrong numbers. The game says "Game Over! The number was 42."

All of them gave the correct output.

## What I Learned
- How to repeat steps using a `while` loop.
- How to make decisions using `if`, `elif` and `else`.
- How to check the user's input so the program does not crash.
- How to keep code neat using a function.
- How to pick a random number using the `random` module.
- Testing again and again makes it easier to find mistakes.
