Here is a simple Python program that generates a random list of numbers and then calculates the sum of all the numbers in the list:

```python
import random

# Function to generate a random list of numbers
def generate_random_list(length):
    random_list = [random.randint(1, 100) for _ in range(length)]
    return random_list

# Function to calculate the sum of numbers in a list
def calculate_sum(numbers):
    total = sum(numbers)
    return total

# Main program
if __name__ == "__main__":
    list_length = 5
    random_numbers = generate_random_list(list_length)
    print("Random numbers generated:", random_numbers)
    
    total_sum = calculate_sum(random_numbers)
    print