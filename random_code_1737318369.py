Here is a simple Python program that generates a random number guessing game. The user has to guess a number between 1 and 10, and the program will provide hints whether the guess is too high or too low until the correct number is guessed.

```python
import random

def guess_number_game():
    secret_number = random.randint(1, 10)
    guess = 0

    print("Welcome to the Number Guessing Game!")
    print("Try to guess the secret number between 1 and 10.")

    while guess != secret_number:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low. Try again!")
        elif guess > secret_number:
            print