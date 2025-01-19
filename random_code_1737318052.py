Here is a simple Python program that generates a random number guessing game. The program will generate a random number between 1 and 100, and the user will have to guess the number within a limited number of attempts.

```python
import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while attempts < max_attempts:
        guess = int(input("Take a guess: "))

        if guess < number_to_guess:
            print("Too low. Try again.")