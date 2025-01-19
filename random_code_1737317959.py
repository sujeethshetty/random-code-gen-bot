Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess it:

```python
import random

def guess_number():
    secret_number = random.randint(1, 10)
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            
            if guess == secret_number:
                print("Congratulations! You guessed the correct number.")
                break
            else:
                print("Try again! The secret number is not", guess)
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_number()
```

In this program:
1. We import the `random`