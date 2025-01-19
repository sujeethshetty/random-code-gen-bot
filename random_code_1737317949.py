Here is a simple Python program that generates a random number guessing game:

```python
import random

def guess_number():
    random_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Can you guess it?")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < random_number:
            print("Too low! Try a higher number.")
        elif user_guess > random_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number in {