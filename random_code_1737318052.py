Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number:

```python
import random

def guess_the_number():
    secret_number = random.randint(1, 10)
    
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess what it is?")
    
    while True:
        guess = input("Enter your guess: ")
        
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess == secret_number:
            print(f"Congratulations! You've guessed the correct number: {secret_number}")