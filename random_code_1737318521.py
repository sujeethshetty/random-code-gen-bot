Here is a simple Python program that generates a random number between 1 and 100 and asks the user to guess it. It provides feedback on whether the guess is too high, too low, or correct. 

```python
import random

def guess_number():
    target_number = random.randint(1, 100)
    
    while True:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        
        if user_guess < target_number:
            print("Too low. Try again!")
        elif user_guess > target_number:
            print("Too high. Try again!")
        else:
            print(f"Congratulations! You guessed the correct number: {target_number}")
            break

guess_number()
``