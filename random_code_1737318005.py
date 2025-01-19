Here is a simple Python program that generates a random number, asks the user to guess it, and provides feedback on whether the guess is correct or not:

```python
import random

def guess_number():
    secret_number = random.randint(1, 100)
    
    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        
        if user_guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif user_guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number()
``