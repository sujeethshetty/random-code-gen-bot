Here's a simple Python program that calculates the factorial of a given number using a recursive function:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
result = factorial(number)

print(f"The factorial of {number} is: {result}")
```

In this program, we define a function `factorial` that calculates the factorial of a number using recursion. We then specify a number (in this case, 5) for which we want to calculate the factorial. The program calls the `factorial` function with the specified number and prints the result.