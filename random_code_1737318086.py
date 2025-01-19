Sure! Here is a simple Python program that generates a random multiplication table for a given number between 1 and 10:

```python
import random

def generate_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

if __name__ == "__main__":
    number = random.randint(1, 10)
    generate_multiplication_table(number)
```

When you run this program, it will pick a random number between 1 and 10, and then generate the multiplication table for that number. The program uses a function `generate_multiplication_table`