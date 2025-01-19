Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def guess_number():
    number = random.randint(1, 10)
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 10. Can you guess it?")
    
    while True:
        guess = int(input("Enter your guess: "))
        
        if guess < number:
            print("Too low, try again!")
        elif guess > number:
            print("Too high, try again!")
        else:
            print("Congratulations! You guessed the correct number.")
            break

    play_again = input("Do you want to play again? (