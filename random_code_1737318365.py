Sure! Here's a simple Python program that generates a random number guessing game:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def guess_number():
    target_number = generate_random_number()

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    while True:
        user_guess = int(input("Enter your guess: "))

        if user_guess < target_number:
            print("Too low. Try again.")
        elif user_guess > target_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the correct number: {target_number