Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def guess_number():
    random_number = generate_random_number()
    while True:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        if user_guess < random_number:
            print("Too low, try again!")
        elif user_guess > random_number:
            print("Too high, try again!")
        else:
            print("Congratulations! You guessed the number correctly.")
            break

guess_number()
```

In this program:
- The `generate_random_number` function generates a random number between 1