Here is a simple Python program that generates a random number and asks the user to guess it. It includes functions, loops, and conditional statements:

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def main():
    random_number = generate_random_number()
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 10. Can you guess it?")

    while guess != random_number:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < random_number:
            print("Too low! Try again