Here is a simple Python program that generates a random number and asks the user to guess it:

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def guess_number():
    random_number = generate_random_number()
    guessed = False

    while not guessed:
        user_guess = int(input("Guess a number between 1 and 10: "))

        if user_guess == random_number:
            print("Congratulations! You guessed the correct number.")
            guessed = True
        elif user_guess < random_number:
            print("Try again. The number is higher.")
        else:
            print("Try again. The number is lower.")

if __name__ == "__main__":
    print("Welcome