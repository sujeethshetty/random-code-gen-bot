Here is a simple Python program that generates a random number and asks the user to guess it. It includes functions, variables, loops, and user input.

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def main():
    random_number = generate_random_number()
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Can you guess it?")

    while guess != random_number:
        guess = int(input("Enter your guess: "))

        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try