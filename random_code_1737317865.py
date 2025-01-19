Here is a simple Python program that generates a random number and allows the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def main():
    random_number = generate_random_number()
    
    print("Welcome to the Random Number Guessing Game!")
    print("I have selected a number between 1 and 10. Can you guess it?")
    
    while True:
        guess = int(input("Enter your guess: "))
        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            break