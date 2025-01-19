Here is a simple Python program that generates and prints a random multiplication table for a specific number:

```python
import random

def generate_multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

def main():
    number = random.randint(1, 10)
    generate_multiplication_table(number)

if __name__ == "__main__":
    main()
```

This program randomly selects a number between 1 and 10, then generates and prints the multiplication table for that number up to 10. You can run this program in a Python environment to see the