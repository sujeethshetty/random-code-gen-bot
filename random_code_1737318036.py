Here is a simple Python program that generates a random number guessing game. The program will ask the user to guess a randomly generated number between 1 and 20. It will provide hints if the user's guess is too high or too low until the correct number is guessed.

```python
import random

def guess_number():
    target_number = random.randint(1, 20)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")

    while True:
        user_guess = int(input("Take a guess: "))

        if user_guess < target_number:
            print("Too low, try again!")
        elif user_guess > target_number:
            print("Too