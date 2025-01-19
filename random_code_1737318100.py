Here is a simple Python program that generates a random number guessing game. The program generates a random number between 1 and 20, and the user has to guess the number within 5 attempts:

```python
import random

def guess_number_game():
    number_to_guess = random.randint(1, 20)
    attempts = 0

    print("Welcome to the Number Guessing Game! You have 5 attempts to guess the number between 1 and 20.")

    while attempts < 5:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too