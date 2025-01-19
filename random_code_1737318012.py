Here is a simple Python program that generates a random number guessing game. The program will generate a random number between 1 and 100, and the user will have to guess the number within a limited number of tries:

```python
import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    max_tries = 5
    tries = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. You have 5 tries to guess it.")

    while tries < max_tries:
        user_guess = int(input("Enter your guess: "))

        if user_guess < number_to_guess:
            print