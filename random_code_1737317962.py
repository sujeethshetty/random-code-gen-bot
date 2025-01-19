Here is a simple Python program that generates a random integer between a specified range and checks if the number is prime:

```python
import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

min_value = 1
max_value = 100

random_number = generate_random_number(min_value, max_value)
print(f"Random number generated: {random_number}")

if is_prime(random_number):
    print("The random number is