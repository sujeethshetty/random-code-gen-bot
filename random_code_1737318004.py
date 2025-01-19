Here is a simple Python program that generates and prints a list of random numbers within a specified range:

```python
import random

def generate_random_numbers(num_count, min_val, max_val):
    random_numbers = []
    for _ in range(num_count):
        random_numbers.append(random.randint(min_val, max_val))
    return random_numbers

def main():
    num_count = 5
    min_val = 1
    max_val = 10

    random_numbers = generate_random_numbers(num_count, min_val, max_val)

    print("Generated random numbers:")
    for num in random_numbers:
        print(num)

if __name__ == "__main__":
    main()
```

In this program:
1. The `generate_random