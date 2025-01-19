Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number:

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def guess_number():
    random_number = generate_random_number()
    
    while True:
        try:
            user_guess = int(input("Guess the number between 1 and 10: "))
            if user_guess == random_number:
                print("Congratulations! You guessed the correct number.")
                break
            else:
                print("Sorry, try again!")
        except ValueError:
            print("Please enter a valid number.")

guess_number()
```

In this program:
- The `generate_random_number()` function generates a