Here is a simple Python program that generates a random number guessing game:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def check_guess(secret_number, guess):
    if guess < secret_number:
        return "Too low!"
    elif guess > secret_number:
        return "Too high!"
    else:
        return "Congratulations! You guessed the number!"

def main():
    secret_number = generate_random_number()
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            result =