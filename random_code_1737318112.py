Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def main():
    random_number = generate_random_number()
    
    print("Welcome to the Number Guessing Game!")
    
    while True:
        user_guess = int(input("Enter your guess (between 1 and 10): "))
        
        if user_guess == random_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif user_guess < random_number:
            print("Try guessing higher.")
        else:
            print("Try guessing lower.")

if __name__ == "__main__":
    main()
```

This program