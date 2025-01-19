Sure! Here is a simple Python program that generates a random number guessing game:

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    
    guess = None
    attempts = 0
    
    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low. Try again!")
        elif guess > number_to_guess:
            print("Too high. Try again!")
    
    print(f"Congratulations! You