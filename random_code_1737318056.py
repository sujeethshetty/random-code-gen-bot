Here is a simple Python program that generates a random number and asks the user to guess it. It includes functions, variables, loops, and conditional statements:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def main():
    random_number = generate_random_number()
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < random_number:
            print("Too low. Try again.")
        elif guess > random_number:
            print("Too high. Try again.")
        else