Here is a simple Python program that generates a random multiplication table for a specific number:

```python
import random

def generate_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

if __name__ == "__main__":
    random_number = random.randint(1, 10)
    generate_multiplication_table(random_number)
```

In this program, we define a function `generate_multiplication_table` that takes a number as input and prints the multiplication table for that number up to 10. We then generate a random number between 1 and 10 using