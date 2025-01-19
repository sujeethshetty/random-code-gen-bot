Here is a simple Python program that generates a list of random numbers and then calculates the mean and standard deviation of those numbers:

```python
import random
import math

def generate_random_numbers(n):
    random_numbers = [random.randint(1, 100) for _ in range(n)]
    return random_numbers

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_standard_deviation(numbers, mean):
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_deviation = math.sqrt(variance)
    return std_deviation

if __name__ == "__main__":
    n = 10
    random_numbers = generate_random_numbers(n)
    
    print