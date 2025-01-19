Here is a simple Python program that generates a random number guessing game:

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low, try again!")
        elif user_guess > number_to_guess:
            print("Too high, try again!")
        else:
            print(f"Congratulations! You've guessed the number in {