Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number:

```python
import random

def guess_number():
    number = random.randint(1, 10)
    
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        
        if guess == number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Try again. Hint: The number is not", "higher" if guess < number else "lower", "than", guess)

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number()
```

In this program