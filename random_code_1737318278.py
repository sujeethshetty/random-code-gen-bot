Sure! Here's a simple Python program that generates a random number and asks the user to guess it. The program will provide hints if the guess is too high or too low:

```python
import random

def guess_the_number():
    number = random.randint(1, 100)
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while guess != number:
        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too low! Try guessing a higher number.")
        elif guess > number:
            print("Too high! Try guessing a lower number.")