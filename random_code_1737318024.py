Here's a simple Python program that generates and prints a random list of numbers and calculates the average of the numbers in the list:

```python
import random

def generate_random_list(length, minimum, maximum):
    random_list = []
    for _ in range(length):
        random_list.append(random.randint(minimum, maximum))
    return random_list

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Generate a random list of 10 numbers between 1 and 100
random_numbers = generate_random_list(10, 1, 100)
print("Random Numbers:", random_numbers)

# Calculate the average of the random numbers
average = calculate_average(random_numbers)
print("