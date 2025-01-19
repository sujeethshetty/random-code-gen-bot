Here's a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def main():
    random_number = generate_random_number()
    guess = None

    print("Welcome to the Random Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    while guess != random_number:
        try:
            guess = int(input("Enter your guess: "))
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
        except ValueError:
            print("Please