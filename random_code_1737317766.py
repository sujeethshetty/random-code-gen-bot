Here is a simple Python program that generates a random multiplication table for a given number:

```python
import random

def generate_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

def main():
    number = random.randint(1, 10)
    generate_multiplication_table(number)

if __name__ == "__main__":
    main()
```

In this program:
- We import the `random` module to generate a random number.
- We define a function `generate_multiplication_table` that takes a number as input and prints its multiplication table up to