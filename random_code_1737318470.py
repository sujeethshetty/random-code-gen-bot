Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def guess_number():
    number = random.randint(1, 100)
    
    while True:
        user_input = input("Guess a number between 1 and 100: ")
        
        if user_input.isdigit():
            guess = int(user_input)
            if guess == number:
                print("Congratulations! You guessed the correct number.")
                break
            elif guess < number:
                print("Try guessing higher.")
            else:
                print("Try guessing lower.")
        else:
            print("Please enter a valid number.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")