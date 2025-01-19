Sure, here is a simple Python program that generates a random number between two user-defined limits and then checks if the number is prime:

```python
import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_random_number(lower_limit, upper_limit):
    return random.randint(lower_limit, upper_limit)

lower_limit = int(input("Enter the lower limit for random number generation: "))
upper_limit = int(input("Enter the upper limit for random number generation: "))

random_number = generate_random_number(lower_limit, upper_limit)