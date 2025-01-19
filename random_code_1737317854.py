Here is a simple Python program that generates a list of random numbers and calculates the average of those numbers:

```python
import random

def generate_random_numbers(num):
    numbers = []
    for _ in range(num):
        numbers.append(random.randint(1, 100))
    return numbers

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

num_of_numbers = 5
random_numbers = generate_random_numbers(num_of_numbers)
print("Generated random numbers:", random_numbers)

average = calculate_average(random_numbers)
print("Average of the random numbers:", average)
```

In this program:
- The `generate_random_numbers` function generates a list of random numbers between 1 and