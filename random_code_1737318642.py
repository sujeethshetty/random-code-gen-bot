Here's a simple Python program that generates and prints a random number between 1 and 10:

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def main():
    random_number = generate_random_number()
    print(f"The random number is: {random_number}")

if __name__ == "__main__":
    main()
```

This program uses the `random` module to generate a random integer between 1 and 10 within the `generate_random_number` function. The main function calls the `generate_random_number` function and prints the random number.