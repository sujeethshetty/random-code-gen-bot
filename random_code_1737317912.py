Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess it?")
    
    while True:
        user_guess = int(input("Enter your guess: "))
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly!")