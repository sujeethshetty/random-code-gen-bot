Here is a simple Python program that generates a random number and asks the user to guess it. It includes functions, variables, loops, and conditional statements:

```python
import random

def guess_number():
    random_number = random.randint(1, 100)
    
    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        
        if user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            break

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number