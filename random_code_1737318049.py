Here is a simple Python program that generates a random list of numbers and calculates the sum of all the numbers in the list:

```python
import random

def generate_random_list(size):
    random_list = []
    for _ in range(size):
        random_list.append(random.randint(1, 100))
    return random_list

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

list_size = 5
random_numbers = generate_random_list(list_size)

print("Random List of Numbers:", random_numbers)
print("Sum of the Numbers:", calculate_sum(random_numbers))
```

In this program:
- The `generate_random_list` function creates a list of random numbers with