Sure! Here's a simple Python program that generates a random number between 1 and 100 and asks the user to guess it. It will provide hints if the guess is too high or too low until the user guesses the correct number:

```python
import random

def guess_number():
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    while True:
        guess = int(input("Enter your guess: "))
        
        if guess < secret_number:
            print("Too low! Try guessing higher.")
        elif guess > secret_number:
            print("Too high! Try