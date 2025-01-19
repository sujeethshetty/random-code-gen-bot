Here is a simple Python program that generates a random multiplication table for a specified number:

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

This program defines a function `generate_multiplication_table(number)` that takes a number as input and prints the multiplication table for that number up to 10. In the `if __name__ == "__main__":` block,