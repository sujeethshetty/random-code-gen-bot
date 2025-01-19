Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number. It will provide hints if the guess is too high or too low, and will keep track of the number of attempts taken to guess the correct number:

```python
import random

def guess_number():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("Guess a number between 1 and 10:")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < secret_number:
            print("Too low, try again.")
        elif user_guess > secret_number:
            print("Too high