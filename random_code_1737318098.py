Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number. It provides feedback on whether the guess is too high, too low, or correct:

```python
import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    guessed = False
    
    print("Welcome to the Number Guessing Game!")
    
    while not guessed:
        user_guess = int(input("Enter your guess (between 1 and 10): "))
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print