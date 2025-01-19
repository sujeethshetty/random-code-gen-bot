Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess it:

```python
import random

def guess_number():
    target_number = random.randint(1, 10)
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 10. Can you guess it?")
    
    while True:
        user_guess = input("Enter your guess: ")
        
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if user_guess == target_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif user_guess <