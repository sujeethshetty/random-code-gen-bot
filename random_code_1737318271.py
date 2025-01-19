Here is a simple Python program that generates a random number between a specified range and asks the user to guess the number:

```python
import random

def guess_number():
    lower_bound = 1
    upper_bound = 10
    secret_number = random.randint(lower_bound, upper_bound)
    
    print(f"Welcome to the Number Guessing Game! I'm thinking of a number between {lower_bound} and {upper_bound}.")
    
    while True:
        user_guess = int(input("Enter your guess: "))
        
        if user_guess < secret_number:
            print("Too low, try again!")
        elif user_guess > secret_number:
            print("Too high, try again!")
        else:
            print(f"Congratulations