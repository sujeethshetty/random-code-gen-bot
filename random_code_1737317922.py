Here is a simple Python program that generates a random multiplication table for a specific number between 1 to 10:

```python
import random

def generate_multiplication_table():
    num = random.randint(1, 10)
    print(f"Multiplication Table for {num}:")
    for i in range(1, 11):
        result = num * i
        print(f"{num} x {i} = {result}")

generate_multiplication_table()
```

This program uses the `random` module to generate a random number between 1 and 10. It then prints out the multiplication table for that number from 1 to 10. The output will vary each time you run the program due to the random number generation