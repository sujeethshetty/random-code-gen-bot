Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number:

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess what it is?")

    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to