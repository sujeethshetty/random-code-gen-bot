Sure! Here's a simple Python program that generates a random number and asks the user to guess it. It will provide hints if the guess is too high or too low:

```python
import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < secret_number:
            print("Too low! Try guessing higher.")
        elif user_guess > secret_number:
            print("Too high