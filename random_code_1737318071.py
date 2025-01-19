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

This program imports the `random` module to generate a random number using the `randint` function within the range of 1 and 10. The program defines a `generate_random_number` function to encapsulate the logic of generating the random number. The `main` function calls the `generate_random_number` function, assigns the result to a variable, and