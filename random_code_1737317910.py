Here is a simple Python program that generates a random number and allows the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def main():
    print("Welcome to the Number Guessing Game!")
    target_number = generate_random_number()
    
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number!")
            break

if __name__ == "__main__":
    main()
```

This program generates