Here's a simple Python program that generates a random number and asks the user to guess it. The program will provide hints if the user's guess is too high or too low:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def guess_the_number():
    random_number = generate_random_number()
    
    while True:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        
        if user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number correctly.")
            break

if __name__