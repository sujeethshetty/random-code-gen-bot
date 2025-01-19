Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number:

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print("Guess a number between 1 and 10:")
    
    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        if user_guess == number_to_guess:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif user_guess < number_to_guess:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

if __