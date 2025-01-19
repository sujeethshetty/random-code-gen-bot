Here is a simple Python program that generates a random list of numbers and then calculates the average of those numbers:

```python
import random

def generate_random_list(length):
    random_list = [random.randint(1, 100) for _ in range(length)]
    return random_list

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Generate a random list of numbers
random_numbers = generate_random_list(5)
print("Random Numbers:", random_numbers)

# Calculate the average of the random numbers
average = calculate_average(random_numbers)
print("Average:", average)
```

In this program, we first define a function `generate_random_list` that generates a list of random