Here is a simple Python program that generates a list of random numbers, calculates their average, and then prints out the numbers and the average:

```python
import random

def generate_random_numbers(n):
    numbers = [random.randint(1, 100) for _ in range(n)]
    return numbers

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

def main():
    n = 5
    random_numbers = generate_random_numbers(n)
    average = calculate_average(random_numbers)

    print("Generated numbers:", random_numbers)
    print("Average of the numbers:", average)

if __name__ == "__main__":
    main()
```

When you run this program, it