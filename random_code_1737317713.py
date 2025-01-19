Here's a simple Python program that generates a random list of numbers and calculates the sum of all even numbers in the list:

```python
import random

def generate_random_list(length):
    random_list = [random.randint(1, 100) for _ in range(length)]
    return random_list

def calculate_sum_of_even_numbers(numbers):
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    return sum_even

list_length = 10
random_numbers = generate_random_list(list_length)
print("Random List of Numbers:", random_numbers)

even_sum = calculate_sum_of_even_numbers(random_numbers)
print("Sum of Even Numbers in the List:", even