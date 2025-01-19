Sure! Here's a simple Python program that generates and prints a random number between 1 and 10:

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def main():
    random_number = generate_random_number()
    print(f"Random number generated: {random_number}")

if __name__ == "__main__":
    main()
```

This program imports the `random` module to generate a random number between 1 and 10 using the `randint()` function. The program defines a function `generate_random_number()` to encapsulate the random number generation logic. The `main()` function then calls this function to generate a random number and prints it to the console.