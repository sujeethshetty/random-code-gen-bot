Here's a simple Python program that generates and prints a random multiplication table:

```python
import random

def generate_multiplication_table():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    print(f"Multiplication Table: {num1} x {num2}")
    
    for i in range(1, 11):
        result = num1 * num2
        print(f"{num1} x {i} = {num1*i}")
    
generate_multiplication_table()
```

This program will randomly select two numbers between 1 and 10, then generate and display the multiplication table for those numbers.