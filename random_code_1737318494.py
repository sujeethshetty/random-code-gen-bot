Here's a simple Python program that calculates the factorial of a number entered by the user:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    number = int(input("Enter a number to calculate its factorial: "))
    
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()
```

This program defines a `factorial` function that recursively calculates the factorial of a given number. The `main` function prompts the user to