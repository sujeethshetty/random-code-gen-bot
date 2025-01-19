Sure! Here's a simple Python program that generates a random number between 1 and 10 and lets the user guess the number. It then provides feedback on whether the guess is correct or not.

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def main():
    random_number = generate_random_number()

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 10. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))

        if guess == random_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Sorry, that