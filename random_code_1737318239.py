Here's a simple Python program that calculates the factorial of a number using a recursive function:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input
num = int(input("Enter a number to calculate its factorial: "))

# Check if the input is a non-negative integer
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num != int(num):
    print("Factorial is not defined for non-integer numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")
```

This program defines a recursive function `