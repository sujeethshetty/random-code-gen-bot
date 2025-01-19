Here is a simple Python program that generates a random number and then asks the user to guess the number:

```python
import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    
    while True:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break