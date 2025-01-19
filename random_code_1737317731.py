Here is a simple Python program that generates a random number guessing game:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def guess_number():
    random_number = generate_random_number()
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")
    
    while True:
        guess = int(input("Enter your guess: "))
        
        if guess < random_number:
            print("Too low! Try guessing higher.")
        elif guess > random_number:
            print("Too high! Try guessing lower.")
        else:
            print("Congratulations! You guessed the correct number.")
            break

if __name