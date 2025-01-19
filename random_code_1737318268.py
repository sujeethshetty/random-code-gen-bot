Here's a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def guess_number():
    random_number = generate_random_number()
    while True:
        user_guess = int(input("Guess the number (between 1 and 10): "))
        if user_guess == random_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Try again. Hint: The number is not", user_guess)

guess_number()
```

This program first generates a random number between 1 and 10 using the `generate_random_number()` function. Then, it prompts the user to