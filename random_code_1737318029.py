Here is a simple Python program that generates a random number between a specified range and asks the user to guess that number:

```python
import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    min_num = 1
    max_num = 10
    target_num = random.randint(min_num, max_num)
    
    while True:
        user_guess = int(input(f"Guess a number between {min_num} and {max_num}: "))
        
        if user_guess < target_num:
            print("Too low! Try again.")
        elif user_guess > target_num:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number: {