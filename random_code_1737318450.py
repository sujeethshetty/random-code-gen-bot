Here is a simple Python program that generates and prints a random multiplication table for a specific number up to a given range:

```python
import random

def generate_multiplication_table(number, range_limit):
    print(f"Multiplication Table for {number}:")
    for i in range(1, range_limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

def main():
    number = random.randint(1, 10)  # Generate a random number between 1 and 10
    range_limit = random.randint(1, 10)  # Generate a random range limit between 1 and 10
    generate_multiplication_table(number, range_limit)