Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def main():
    random_number = generate_random_number()
    guess = 0

    print("Welcome to the Number Guessing Game!")
    
    while guess != random_number:
        try:
            guess = int(input("Guess the number (between 1 and 100): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
    
    print("Congratulations