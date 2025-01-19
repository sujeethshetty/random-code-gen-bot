Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try guessing higher.")
        elif guess > secret_number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulations! You guessed the number in {at