Here is a simple Python program that generates a random number and asks the user to guess it. It includes functions, variables, loops, and conditional statements:

```python
import random

def generate_random_number():
    return random.randint(1, 20)

def guess_number():
    random_number = generate_random_number()
    
    print("I have selected a number between 1 and 20. Can you guess it?")
    
    while True:
        user_guess = int(input("Enter your guess: "))
        
        if user_guess < random_number:
            print("Too low, try again!")
        elif user_guess > random_number:
            print("Too high, try again!")
        else:
            print("Congratulations! You guessed the correct number