Here is a simple Python program that generates a random number and asks the user to guess it. The program will provide hints if the guess is too high or too low:

```python
import random

def guess_number():
    secret_number = random.randint(1, 100)
    
    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        
        if user_guess < secret_number:
            print("Too low, try again!")
        elif user_guess > secret_number:
            print("Too high, try again!")
        else:
            print("Congratulations! You guessed the correct number.")
            break

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")