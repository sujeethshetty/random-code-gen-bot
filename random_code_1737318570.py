Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number. It then provides feedback on whether the guess is too high, too low, or correct.

```python
import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    guessed = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess it?\n")

    while not guessed:
        user_guess = int(input("Enter your guess: "))

        if user_guess == number_to_guess:
            print("Congratulations! You guessed the correct number.")
            guessed = True