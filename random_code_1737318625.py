Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def main():
    random_number = generate_random_number()
    guess = None

    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != random_number:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < random_number:
            print("Too low. Try again.")
        elif guess > random_number:
            print("Too high. Try