Here is a simple Python program that generates a random number between a specified range and checks if the user's guess matches the generated number:

```python
import random

def generate_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

def check_guess(random_num, guess):
    if random_num == guess:
        return True
    else:
        return False

min_range = 1
max_range = 10

random_num = generate_random_number(min_range, max_range)

print("Welcome to the Number Guessing Game!")
print(f"I have selected a number between {min_range} and {max_range}. Can you guess it?")

while True:
    user_guess = int(input("Enter your guess: