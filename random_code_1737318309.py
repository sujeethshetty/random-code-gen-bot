Sure! Here's a simple Python program that generates a random number guessing game:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def guess_number():
    random_number = generate_random_number()
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    while True:
        user_guess = int(input("Enter your guess: "))
        
        if user_guess < random_number:
            print("Too low, try guessing higher.")
        elif user_guess > random_number:
            print("Too high, try guessing lower.")
        else:
            print("Congratulations! You guessed the correct number.")