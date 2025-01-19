Here's a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number. It includes a loop for multiple guesses and a function to check if the guess is correct:

```python
import random

def guess_number():
    secret_number = random.randint(1, 10)
    
    while True:
        user_guess = int(input("Guess the number (between 1 and 10): "))
        
        if user_guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Try again. Incorrect guess.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number()
```