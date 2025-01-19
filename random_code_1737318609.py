Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    
    while True:
        user_guess = int(input("Guess a number between 1 and 10: "))
        
        if user_guess == number_to_guess:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Oops! Try again.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number()
```

In this program:
- We import the `random` module to generate a random number.
- The `guess_number` function