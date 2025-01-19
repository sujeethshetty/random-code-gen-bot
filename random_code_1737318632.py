Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number. The program will provide feedback on whether the guess is too high, too low, or correct.

```python
import random

def guess_number():
    secret_number = random.randint(1, 10)
    guess = None

    while guess != secret_number:
        guess = int(input("Guess the secret number (between 1 and 10): "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
    
    print("Congratulations! You guessed the secret number {} correctly!".format(secret_number))

guess