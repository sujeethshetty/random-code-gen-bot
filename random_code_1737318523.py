Here is a simple Python program that generates a random number and asks the user to guess it. It includes functions, variables, loops, and user input.

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def guess_number():
    random_number = generate_random_number()
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == random_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Try again!")

guess_number()
```

In this program:
- We import the `random` module to generate a random number.
- The `generate_random_number` function generates a random number