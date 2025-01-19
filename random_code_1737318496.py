Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number. It provides feedback on whether the guess is too high, too low, or correct.

```python
import random

def guess_number():
    secret_number = random.randint(1, 10)
    guessed = False

    while not guessed:
        guess = int(input("Guess a number between 1 and 10: "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            guessed = True

if __name__ == "__