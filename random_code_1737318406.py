Here's a simple Python program that generates a random number guessing game. The program will generate a random number between 1 and 20, and the user will have 5 chances to guess the correct number. After each guess, the program will provide a hint if the guess is higher or lower than the random number.

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 20)
    attempts = 5

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 20. You have 5 attempts to guess it.")

    while attempts > 0:
        guess = int(input("Enter your guess: "))

        if guess