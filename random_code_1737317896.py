Sure! Here's a simple Python program that generates a random number and asks the user to guess it. It provides hints if the guessed number is higher or lower than the actual number:

```python
import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Can you guess it?")
    
    while True:
        user_guess = int(input("Enter your guess: "))
        
        if user_guess < number_to_guess:
            print("Too low! Try guessing a higher number.")
        elif user_guess > number_to_guess:
            print("Too high! Try guessing