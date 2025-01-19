Sure, here's a simple Python program that calculates the factorial of a number entered by the user:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number to calculate its factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    result = factorial(number)
    print(f"The factorial of {number} is {result}")
```

This program defines a `factorial` function that recursively calculates the factorial of a number. It then prompts the user to