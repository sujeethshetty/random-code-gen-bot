Here is a simple Python program that generates a random number and asks the user to guess it. It includes functions, variables, loops, and user input handling:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    target_number = generate_random_number()
    print("I've selected a number between 1 and