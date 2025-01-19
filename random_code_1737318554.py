Here is a simple Python program that generates a random number guessing game:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def guess_number():
    random_number = generate_random_number()
    
    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        
        if user_guess < random_number:
            print("Too low, try again!")
        elif user_guess > random_number:
            print("Too high, try again!")
        else:
            print("Congratulations! You guessed the correct number.")
            break

if __name__ == "__main__":
    print("Welcome to the Random Number Guessing Game!")
    guess_number()
```

This program