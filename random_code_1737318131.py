Here is a simple Python program that calculates the factorial of a given number using a recursive function:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input for the number
num = int(input("Enter a number to calculate its factorial: "))

# Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")
```

In this program, the `factorial` function calculates the factorial of a number using recursion. The user is prompted to enter a