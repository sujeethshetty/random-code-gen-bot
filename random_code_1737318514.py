Here's a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number. It then provides feedback on whether the guess is correct or not.

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    
    while True:
        user_guess = input("Guess a number between 1 and 10: ")
        
        if user_guess.isdigit():
            user_guess = int(user_guess)
            
            if user_guess == number_to_guess:
                print("Congratulations! You guessed the correct number.")
                break
            else:
                print("Sorry, try again!")
        else:
            print("Please enter a valid number.")

if __name__