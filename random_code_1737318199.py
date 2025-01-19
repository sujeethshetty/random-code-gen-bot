Here is a simple Python program that generates and prints a random number between 1 and 10. It uses the `random` module to generate random numbers.

```python
import random

def generate_random_number():
    return random.randint(1, 10)

def main():
    random_number = generate_random_number()
    print("Random number generated: {}".format(random_number))

if __name__ == "__main__":
    main()
```

This program defines a function `generate_random_number()` that uses `random.randint()` to generate a random number between 1 and 10. The `main()` function calls `generate_random_number()` and prints the generated random number. When you run the program, it will output a random number between 1