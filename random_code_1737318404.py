Here's a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number. The program will provide feedback if the guess is correct or not.

```python
import random

def guess_number():
    secret_number = random.randint(1, 10)
    
    while True:
        user_guess = input("Guess a number between 1 and 10: ")
        
        if user_guess.isdigit():
            user_guess = int(user_guess)
            
            if user_guess == secret_number:
                print("Congratulations! You guessed the correct number.")
                break
            else:
                print("Wrong guess. Try again.")
        else:
            print("Please enter a valid number.")

if __name__ ==