Here is a simple Python program that generates a random list of numbers and then calculates the sum of all the numbers in the list:

```python
import random

def generate_random_list(size):
    random_list = [random.randint(1, 100) for _ in range(size)]
    return random_list

def calculate_sum(numbers):
    total = sum(numbers)
    return total

if __name__ == "__main__":
    list_size = 5
    random_numbers = generate_random_list(list_size)
    print("Generated random list:", random_numbers)

    total_sum = calculate_sum(random_numbers)
    print("Sum of all numbers in the list:", total_sum)
```

In this program:
- The `generate_random_list` function generates