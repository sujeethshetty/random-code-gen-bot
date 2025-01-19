Here is a simple Python program that generates a random number and asks the user to guess it. It provides feedback if the guess is too high or too low until the correct number is guessed.

```python
import random

def guess_number():
    number = random.randint(1, 100)
    
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the correct number: {number}")
            break

guess_number()
```

This program uses the `random` module to generate a random