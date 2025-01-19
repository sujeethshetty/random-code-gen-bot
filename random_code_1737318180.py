Here's a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def main():
    print("Welcome to the Guess the Number Game!")
    random_number = generate_random_number()

    while True:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == random_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Sorry, that's not the correct number. Try again.")

if __name__ == "__main__":
    main()
```

In this program:
- We import the `random` module to generate