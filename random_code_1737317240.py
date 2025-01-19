Here is a simple Python program that generates a random number and asks the user to guess it. It includes functions, variables, loops, and conditional statements:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def main():
    random_number = generate_random_number()
    guess = None
    
    print("Welcome to the Number Guessing Game!")
    
    while guess != random_number:
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
    
    print(f"Congratulations! You guessed the correct number {