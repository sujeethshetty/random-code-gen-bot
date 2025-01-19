Here's a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number. It then provides feedback on whether the guess is correct or not.

```python
import random

def guess_number():
    target_number = random.randint(1, 10)
    
    while True:
        user_guess = int(input("Guess a number between 1 and 10: "))
        
        if user_guess == target_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Sorry, that's not the correct number. Try again.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number()
```