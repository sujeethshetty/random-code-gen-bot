Here is a simple Python program that generates and prints a random number within a specified range:

```python
import random

def generate_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

min_num = 1
max_num = 100

random_number = generate_random_number(min_num, max_num)
print(f"Random number between {min_num} and {max_num}: {random_number}")
```

In this program, we define a function `generate_random_number` that takes two parameters `min_num` and `max_num` and returns a random integer within that range using the `randint` function from the `random` module.

We then set the minimum and maximum values for the range, generate