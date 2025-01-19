Here is a simple Python program that generates a list of random numbers and calculates their average:

```python
import random

def generate_random_numbers(n):
    numbers = [random.randint(1, 100) for _ in range(n)]
    return numbers

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

def main():
    n = 5  # Number of random numbers to generate
    random_numbers = generate_random_numbers(n)
    print("Generated random numbers:", random_numbers)

    avg = calculate_average(random_numbers)
    print("Average of the random numbers:", avg)

if __name__ == "__main__":
    main()
```

In this program:
- The `