Certainly! Here's a simple Python program that calculates the factorial of a number using a recursive function:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    num = int(input("Enter a number to calculate its factorial: "))
    
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"The factorial of {num} is: {result}")

if __name__ == "__main__":
    main()
```

This program defines a `factorial` function that calculates the factorial of a given number using recursion. The `main`