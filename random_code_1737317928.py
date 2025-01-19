Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number. It will provide hints to guide the user to the correct answer.

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Try guessing a bit higher.")
        elif user_guess > number_to_guess: