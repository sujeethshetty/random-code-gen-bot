Here's a simple Python program that generates a random number guessing game:

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    
    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        
        if user_guess < number_to_guess:
            print("Too low, try again!")
        elif user_guess > number_to_guess:
            print("Too high, try again!")
        else:
            print("Congratulations! You guessed the correct number.")
            break

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number()
```

In this program, a random number between 1 and