Sure! Here is a simple Python program that generates a random number guessing game:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def check_guess(random_number, guess):
    if guess < random_number:
        return "Too low. Try again."
    elif guess > random_number:
        return "Too high. Try again."
    else:
        return "Congratulations! You guessed the number."

def main():
    random_number = generate_random_number()
    print("I have selected a random number between 1 and 100. Try to guess it!")

    while True:
        guess = int(input("Enter your guess: "))

        result = check_guess(random_number, guess)
        print