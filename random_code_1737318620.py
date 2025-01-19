Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number. It then provides feedback on whether the guess is correct or not:

```python
import random

def guess_number():
    secret_number = random.randint(1, 10)
    
    while True:
        user_guess = input("Guess the number between 1 and 10: ")
        
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        user_guess = int(user_guess)
        
        if user_guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Incorrect. Try again!")

if __name__ ==