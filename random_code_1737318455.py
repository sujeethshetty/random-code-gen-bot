Here is a simple Python program that generates and prints a random multiplication table for a given number:

```python
import random

def generate_multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

def main():
    random_number = random.randint(1, 10)
    generate_multiplication_table(random_number)

if __name__ == "__main__":
    main()
```

This program first generates a random number between 1 and 10. It then calls the `generate_multiplication_table` function to create and print the multiplication table for that random number. The