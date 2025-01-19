Here is a simple Python program that generates a random number between a specified range and then checks if the number is even or odd:

```python
import random

def generate_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

min_num = 1
max_num = 100

random_num = generate_random_number(min_num, max_num)

print(f"The random number generated is: {random_num}")
print(f"The number is {check_even_odd(random_num)}.")
```

In this program:
- The `generate_random_number` function generates a random number between `