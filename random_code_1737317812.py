Here is a simple Python program that generates a random number guessing game. The user needs to guess a randomly generated number between 1 and 10:

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
            print("Incorrect guess. Try again.")

if __name__ == "__main__":
    print("Welcome to the Random Number Guessing Game!")
    guess_number()
```

To play