Here is a simple Python program that generates a random number and allows the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def main():
    random_number = generate_random_number()
    
    print("Guess the random number between 1 and 100!")
    
    while True:
        guess = int(input("Enter your guess: "))
        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            break

if __name__ == "__main__":
    main()
```

In this program, a