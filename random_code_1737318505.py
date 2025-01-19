Here is a simple Python program that generates a random multiplication table for a specific number:

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

This program first generates a random number between 1 and 10. Then, it calls the `generate_multiplication_table` function to create a multiplication table for that random number. The function uses a loop to