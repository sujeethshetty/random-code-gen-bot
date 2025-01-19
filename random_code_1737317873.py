Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def generate_number():
    return random.randint(1, 10)

def main():
    number_to_guess = generate_number()
    
    print("Welcome to the Number Guessing Game!")
    
    while True:
        user_guess = int(input("Guess a number between 1 and 10: "))
        
        if user_guess == number_to_guess:
            print("Congratulations! You guessed the correct number.")
            break
        elif user_guess < number_to_guess:
            print("Try again! The number is higher.")
        else:
            print("Try again! The number is lower.")

if __name__ == "__main