# Project Summary: Number Guessing Game

**Introduction**
This project is a small game I made using Python 3. The computer picks a secret number between 1 and 100, and I try to guess it. I get only 5 tries. After every guess, the game tells me if my number is "Too high" or "Too low", so I can guess better next time.

**Why I made it**
I made this project to practice the basics of Python. It helped me understand how loops, conditions, functions, and the random module work together in a real program.

**How the game works**
1. The computer picks a secret number using the random module. For testing, I fixed it to 42.
2. The game asks me to type my guess.
3. It checks my input. If I type letters like "abc", it shows "Invalid input. Enter a whole number." If I type a number like 150, it shows "Out of range. Enter a number between 1 and 100." In both cases, I do not lose a try.
4. If the input is correct, it counts as one try. The game then shows "Too low!", "Too high!", or "Congratulations!" along with the attempts left.
5. If I use all 5 tries without guessing right, the game shows "Game Over!" and tells me the secret number.
6. At the end, it shows how many attempts I used and asks "Play again? (y/n)".

**Concepts used**
- **Loop:** a `while` loop repeats the steps until the 5 tries are finished.
- **Conditions:** `if`, `elif`, and `else` decide which message to show.
- **Function:** `play_game()` keeps all the game steps in one place.
- **Random:** `random.randint(1, 100)` picks the secret number.

**Testing**
I tested the game with all 4 test cases from the project sheet:
- **Test 1:** guessing 42 wins the game in 1 attempt.
- **Test 2:** guessing 1 and then 100 gives "Too low" and "Too high", and the attempts left go down.
- **Test 3:** typing "abc" and then 150 shows error messages, and all 5 attempts stay safe.
- **Test 4:** guessing 10, 90, 50, 30, 20 gives the hints and ends with "Game Over! The number was 42."

All the tests gave the correct output.

**What I learned**
I learned how to repeat steps using a loop, how to check user input so the program does not break, and how to keep my code clean using a function. I also learned how important testing is.

**Conclusion**
The game works well and follows all the project requirements. It is simple, easy to understand, and a good first project for learning Python.
