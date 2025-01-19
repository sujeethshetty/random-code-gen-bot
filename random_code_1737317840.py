Here's a simple Python program that calculates the factorial of a given number using a recursive function:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
result = factorial(number)

print(f'The factorial of {number} is: {result}')
```

In this program, we define a `factorial` function that calculates the factorial of a number recursively. We then call this function with the number 5 and print out the result. You can easily modify the `number` variable to calculate the factorial for a different number.