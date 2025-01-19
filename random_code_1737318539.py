Sure! Here is a simple Python program that generates a random list of numbers, calculates the sum of all numbers in the list, and then determines if the sum is an even or odd number:

```python
import random

def generate_random_numbers(num_elements):
    numbers = [random.randint(1, 100) for _ in range(num_elements)]
    return numbers

def calculate_sum(numbers):
    return sum(numbers)

def check_even_odd(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'

num_elements = 5
random_numbers = generate_random_numbers(num_elements)
print(f"Generated numbers: {random_numbers}")

total_sum = calculate_sum(random_numbers)
print(f"