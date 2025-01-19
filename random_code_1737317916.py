Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    guess = None
    
    while guess != number_to_guess:
        try:
            guess = int(input("Guess the number (between 1 and 10): "))
        
            if guess < number_to_guess:
                print("Too low, try again.")
            elif guess > number_to_guess:
                print("Too high, try again.")
            else:
                print("Congratulations! You guessed the number.")
        
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    print("Welcome