Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess it. The program will provide feedback on whether the guess is too high, too low, or correct.

```python
import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    
    while True:
        user_guess = int(input("Guess the number (between 1 and 10): "))
        
        if user_guess < number_to_guess:
            print("Too low, try again.")
        elif user_guess > number_to_guess:
            print("Too high, try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            break

guess_the_number()