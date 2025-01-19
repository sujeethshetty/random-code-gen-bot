Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number. It provides hints if the user's guess is too high or too low until they guess the correct number:

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    
    while True:
        user_guess = int(input("Guess the number between 1 and 10: "))
        
        if user_guess == number_to_guess:
            print("Congratulations! You guessed the correct number.")
            break
        elif user_guess < number_to_guess:
            print("Try again. The number is higher.")
        else:
            print("Try again. The number is lower