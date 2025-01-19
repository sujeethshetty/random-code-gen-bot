Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number:

```python
import random

def guess_number():
    secret_number = random.randint(1, 10)
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 10. Can you guess it?")
    
    while True:
        guess = int(input("Enter your guess: "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            break

if __name__