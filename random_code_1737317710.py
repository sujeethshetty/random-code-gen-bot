Here's a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number:

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 10): "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    random_number = generate_random_number()
    
    print("Guess the random number between 1 and 10!")
    
    while