Here's a simple Python program that generates a random multiplication table for a given number:

```python
import random

def generate_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

if __name__ == "__main__":
    random_number = random.randint(1, 10)
    generate_multiplication_table(random_number)
```

This program defines a function `generate_multiplication_table` that takes a number as input and prints out the multiplication table for that number from 1 to 10. In the main block, a random number between 1 and