Sure! Here's a simple Python program that generates a random number guessing game:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def guess_number():
    random_number = generate_random_number()
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < random_number:
            print("Too low. Try again.")
        elif guess > random_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You