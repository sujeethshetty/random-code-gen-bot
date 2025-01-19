Here is a simple Python program that generates a random list of 10 numbers, then calculates the sum of the numbers in the list:

```python
import random

def generate_random_list():
    random_list = []
    for _ in range(10):
        random_list.append(random.randint(1, 100))
    return random_list

def calculate_sum(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum

random_numbers = generate_random_list()
print("Random numbers:", random_numbers)

total = calculate_sum(random_numbers)
print("Sum of the numbers:", total)
```

This program first generates a list of 10 random numbers between 1 and 100. Then,