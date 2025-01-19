Here's a simple Python program that generates a list of random numbers and then calculates the average value of those numbers:

```python
import random

def generate_random_numbers(num):
    return [random.randint(1, 100) for _ in range(num)]

def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers) if len(numbers) > 0 else 0

num_of_numbers = 5
random_numbers = generate_random_numbers(num_of_numbers)
print(f"Random numbers: {random_numbers}")

average = calculate_average(random_numbers)
print(f"Average of random numbers: {average}")
```

In this program:
- We define a function `generate_random_numbers(num)` that generates a list of `num