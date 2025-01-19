Here is a simple Python program that generates a random positive integer and checks if it is a prime number:

```python
import random

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_random_number():
    return random.randint(1, 100)

random_number = generate_random_number()
print(f"Random number generated: {random_number}")

if is_prime(random_number):
    print(f"{random_number} is a prime number.")
else:
    print(f"{random_number} is not a prime number.")
```

In this program