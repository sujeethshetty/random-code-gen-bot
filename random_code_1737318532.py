Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number. It then provides feedback on whether the guess is correct or not.

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def main():
    random_number = generate_random_number()

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        user_guess = int(input("Enter your guess: "))

        if user_guess == random_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Sorry, that's not the correct