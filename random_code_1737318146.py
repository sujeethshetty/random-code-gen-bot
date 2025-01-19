Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number:

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def main():
    random_number = generate_random_number()
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 10. Can you guess it?")
    
    while True:
        guess = int(input("Enter your guess: "))
        
        if guess == random_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < random_number:
            print("Try again. The number is higher.")
        else: