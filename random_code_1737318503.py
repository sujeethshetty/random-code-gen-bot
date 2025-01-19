Here is a simple Python program that calculates the factorial of a given number using a recursive function:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input for the number
num = int(input("Enter a number to calculate its factorial: "))

# Check if the input is a non-negative integer
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif not isinstance(num, int):
    print("Factorial is only defined for integers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
```

This program defines a recursive function