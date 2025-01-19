Sure! Here's a simple Python program that generates a random number between 1 and 10 and allows the user to guess the number. It will inform the user if their guess is too high, too low, or correct.

```python
import random

def guess_number():
    secret_number = random.randint(1, 10)
    
    while True:
        user_guess = int(input("Guess a number between 1 and 10: "))
        
        if user_guess < secret_number:
            print("Too low. Try again.")
        elif user_guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            break

if __name__ == "__main