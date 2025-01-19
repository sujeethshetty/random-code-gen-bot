Here is a simple Python program that generates and prints a random number between a user-specified range:

```python
import random

def generate_random_number():
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    random_number = random.randint(lower_bound, upper_bound)
    
    return random_number

def main():
    random_number = generate_random_number()
    
    print(f"Random number generated: {random_number}")

if __name__ == "__main__":
    main()
```

In this program:
- The `generate_random_number` function prompts the user to input a lower and upper bound for the random number range, generates a random