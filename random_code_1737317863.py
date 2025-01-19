Sure! Here's a simple Python program that generates a random number and asks the user to guess it. It includes functions, variables, loops, and conditional statements:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def guess_number():
    random_number = generate_random_number()
    attempts = 0

    while True:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        if user_guess < random_number:
            print("Too low. Try again.")
        elif user_guess > random_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {