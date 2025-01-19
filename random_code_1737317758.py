Here is a simple Python program that generates a random number between 1 and 10 and lets the user guess the number. The program will provide feedback on whether the guess is correct, too high, or too low.

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    
    while True:
        try:
            user_guess = int(input("Guess the number between 1 and 10: "))
            
            if user_guess == number_to_guess:
                print("Congratulations! You guessed the correct number.")
                break
            elif user_guess < number_to_guess:
                print("Too low. Try guessing higher.")
            else:
                print("Too high. Try guessing lower.")