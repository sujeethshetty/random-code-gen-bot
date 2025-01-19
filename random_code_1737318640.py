Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def get_user_guess():
    while True:
        try:
            guess = int(input("Guess the number (between 1 and 10): "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    random_number = generate_random_number()
    print("Welcome to the Number Guessing Game!")
    
    while True:
        user_guess = get_user