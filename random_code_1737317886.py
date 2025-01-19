Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def main():
    random_number = generate_random_number()
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Can you guess it?")
    
    while True:
        guess = int(input("Enter your guess: "))
        
        if guess < random_number:
            print("Too low. Try guessing higher!")
        elif guess > random_number:
            print("Too high. Try guessing lower!")
        else:
            print("Congratulations! You guessed the correct number.")