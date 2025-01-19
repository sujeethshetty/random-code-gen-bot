Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number:

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10...")
    
    while True:
        user_guess = int(input("Take a guess: "))
        
        if user_guess == number_to_guess:
            print("Congratulations! You guessed the correct number.")
            break
        elif user_guess < number_to_guess:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __