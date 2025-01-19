Here is a simple Python program that generates a random number guessing game:

```python
import random

def guess_number():
    number = random.randint(1, 10)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low, try again!")
        elif guess > number:
            print("Too high, try again!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __