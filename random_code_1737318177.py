Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def guess_number():
    random_number = generate_random_number()
    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        if guess < random_number:
            print("Too low, try again!")
        elif guess > random_number:
            print("Too high, try again!")
        else:
            print("Congratulations! You guessed the correct number.")
            break

guess_number()
```

In this program:
- We import the `random` module to generate a random number.
- We define a