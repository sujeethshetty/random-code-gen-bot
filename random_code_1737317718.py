Here is a simple Python program that generates a random number guessing game:

```python
import random

def guess_number():
    secret_number = random.randint(1, 20)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20. Can you guess it?")

    while attempts < 5:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts+1} attempts.")
            break