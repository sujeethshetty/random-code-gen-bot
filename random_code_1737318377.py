Certainly! Here's a simple Python program that generates and prints a random multiplication table for a specified number of rows and columns:

```python
import random

def generate_multiplication_table(rows, columns):
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            result = i * j
            print(f"{i} * {j} = {result}")

rows = random.randint(1, 10)
columns = random.randint(1, 10)

print(f"Generating a {rows}x{columns} multiplication table:")
generate_multiplication_table(rows, columns)
```

This program first imports the `random` module to generate random numbers for the rows and columns