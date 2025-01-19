Here is a simple Python program that generates a random number and checks if it is even or odd:

```python
import random

def generate_random_number():
    return random.randint(1, 100)

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    random_number = generate_random_number()
    print("Generated random number:", random_number)
    
    result = check_even_odd(random_number)
    print("The number is:", result)

if __name__ == "__main__":
    main()
```

In this program:
- We import the `random` module to generate random numbers.
- We define three functions: `generate_random_number