Here's a simple Python program that generates a random number guessing game. The user has to guess a number between 1 and 10, and the program will provide hints if the guess is too high or too low. Once the correct number is guessed, the program will congratulate the user.

```python
import random

def guess_number():
    target_number = random.randint(1, 10)
    guess = None
    
    print("Guess a number between 1 and 10:")
    
    while guess != target_number:
        guess = int(input("Enter your guess: "))
        
        if guess < target_number:
            print("Too low. Try again.")
        elif guess > target_number:
            print("Too high. Try again.")