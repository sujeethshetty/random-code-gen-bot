Here is a simple Python program that generates and prints a random multiplication table for a specified number:

```python
import random

def generate_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

if __name__ == "__main__":
    random_number = random.randint(1, 10)  # Generate a random number between 1 and 10
    generate_multiplication_table(random_number)
```

When you run this program, it will generate a random number between 1 and 10, then it will display the multiplication table for that number from