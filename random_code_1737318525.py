Here's a simple Python program that generates a random number guessing game. The user has to guess a number between 1 and 10, and the program will provide feedback on whether the guess is too high, too low, or correct.

```python
import random

def guess_the_number():
    hidden_number = random.randint(1, 10)

    while True:
        user_guess = int(input("Guess the number (between 1 and 10): "))

        if user_guess < hidden_number:
            print("Too low! Try again.")
        elif user_guess > hidden_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number.")
            break

if __name__ ==