Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def get_user_guess():
    while True:
        try:
            guess = int(input("Guess the number (between 1 and 10): "))
            return guess
        except ValueError:
            print("Please enter a valid number.")

def main():
    random_number = generate_random_number()
    
    while True:
        user_guess = get_user_guess()
        
        if user_guess == random_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Sorry, try again!")

if __name__ ==