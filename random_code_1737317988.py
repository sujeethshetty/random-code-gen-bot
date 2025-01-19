Here is a simple Python program that generates a random number and asks the user to guess it. It includes functions, variables, loops, and conditional statements:

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
            print("Try again. Hint: The number is {}".format("greater" if user_guess < random_number else "less"))

if __name__ == "__main__":
    print("