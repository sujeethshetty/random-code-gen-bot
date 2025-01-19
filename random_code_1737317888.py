Here is a simple Python program that generates a random multiplication table for a given number:

```python
import random

def generate_multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

def main():
    number = random.randint(1, 10)
    generate_multiplication_table(number)

if __name__ == "__main__":
    main()
```

When you run this program, it will generate a random number between 1 and 10, and then display the multiplication table for that number. The table will show the multiplication of the number with each integer from