Sure! Here's a simple Python program that generates and prints a random list of numbers and then calculates their sum:

```python
import random

def generate_random_numbers(length):
    numbers = [random.randint(1, 100) for _ in range(length)]
    return numbers

def calculate_sum(numbers):
    total = sum(numbers)
    return total

def main():
    length = 5
    random_numbers = generate_random_numbers(length)
    print("Random Numbers:", random_numbers)

    total_sum = calculate_sum(random_numbers)
    print("Sum of the Numbers:", total_sum)

if __name__ == "__main__":
    main()
```

In this program:
- The `generate_random_numbers` function generates a list of random numbers