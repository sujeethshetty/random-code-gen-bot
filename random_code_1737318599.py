Here is a simple Python program that generates a random number guessing game:

```python
import random

def guess_number():
    secret_number = random.randint(1, 20)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 20. Can you guess it?")
    
    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        if user_guess < secret_number:
            print("Too low! Try guessing higher.")
        elif user_guess > secret_number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulations! You guessed the number in {attempts}