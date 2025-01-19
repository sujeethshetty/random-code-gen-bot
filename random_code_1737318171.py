Here is a simple Python program that generates a random number guessing game:

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        user_guess = int(input("Enter your guess: "))
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            break

if __name__ == "__main__":
    guess_number()
```