Here is a simple Python program that generates a random number and asks the user to guess it. The program will provide hints if the user's guess is too high or too low:

```python
import random

def guess_the_number():
    number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))
        
        if guess < number:
            print("Too low! Try guessing higher.")
        elif guess > number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulations! You guessed the