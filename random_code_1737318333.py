Sure! Here's a simple Python program that calculates the factorial of a number entered by the user:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number to calculate its factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
```

In this program, we define a function `factorial` that calculates the factorial of a given number using recursion. We