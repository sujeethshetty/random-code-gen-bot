Here's a simple Python program that generates a random number guessing game. The user will have to guess a randomly generated number within a specified range:

```python
import random

def generate_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

def guess_number(min_num, max_num):
    random_num = generate_random_number(min_num, max_num)
    
    print(f"Welcome to the Number Guessing Game! I'm thinking of a number between {min_num} and {max_num}. Can you guess it?")
    
    while True:
        user_guess = int(input("Enter your guess: "))
        
        if user_guess < random_num:
            print("Too low! Try again.")
        elif user_guess