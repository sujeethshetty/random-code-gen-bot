Here's a simple Python program that generates a random number guessing game. The player has to guess a randomly generated number within a specified range. The program gives hints if the player's guess is too high or too low.

```python
import random

def guess_the_number():
    lower_bound = 1
    upper_bound = 100
    target_number = random.randint(lower_bound, upper_bound)
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. Can you guess it?")
    
    while True:
        user_guess = int(input("Enter your guess: "))
        
        if user_guess < target_number:
            print("Too low! Try