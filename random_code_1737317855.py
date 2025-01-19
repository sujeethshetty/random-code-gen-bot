Here is a simple Python program that generates a random list of numbers and calculates the sum of even numbers in the list:

```python
import random

def generate_random_list(length):
    random_list = [random.randint(1, 100) for _ in range(length)]
    return random_list

def calculate_sum_of_even_numbers(numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    return even_sum

# Generate a random list of 10 numbers
random_numbers = generate_random_list(10)
print("Random Numbers:", random_numbers)

# Calculate the sum of even numbers in the list
even_sum = calculate_sum_of_even_numbers(random_numbers