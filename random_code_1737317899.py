Sure! Here's a simple Python program that generates and prints a random multiplication table for a given number:

```python
import random

def generate_multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

if __name__ == "__main__":
    random_number = random.randint(1, 10)
    generate_multiplication_table(random_number)
```

In this program:
- We import the `random` module to generate a random number.
- We define a function `generate_multiplication_table(number)` that takes a number as input and prints the multiplication table for