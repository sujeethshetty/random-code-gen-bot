Sure! Here is a simple Python program that calculates the factorial of a given number using a recursive function:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input for the number
num = int(input("Enter a number to calculate its factorial: "))

# Check if the input number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
```

This program defines a function `factorial` that calculates the factorial of a given number recursively. It then takes user