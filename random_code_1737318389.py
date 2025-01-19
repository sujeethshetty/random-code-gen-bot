Here's a simple Python program that generates a random number between 1 and 10 and asks the user to guess it. The program will provide feedback on whether the guess is too high, too low, or correct.

```python
import random

def guess_number():
    target_number = random.randint(1, 10)
    
    while True:
        user_guess = int(input("Guess a number between 1 and 10: "))
        
        if user_guess < target_number:
            print("Too low! Try again.")
        elif user_guess > target_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            break

guess_number()
```

In this program: