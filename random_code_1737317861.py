Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def guess_number():
    random_number = generate_random_number()
    
    while True:
        guess = int(input("Guess the number (between 1 and 10): "))
        
        if guess < random_number:
            print("Too low, try again!")
        elif guess > random_number:
            print("Too high, try again!")
        else:
            print("Congratulations! You guessed the number.")
            break

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number()
```

In