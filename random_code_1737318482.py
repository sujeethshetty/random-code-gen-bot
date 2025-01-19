Sure! Here's a simple Python program that calculates the factorial of a number entered by the user:

```python
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def main():
    num = int(input("Enter a number to calculate its factorial: "))
    
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"The factorial of {num} is {result}")

if __name__ == "__main__":
    main()
```

In this program, the `factorial` function calculates the factorial of a number recursively. The `main` function takes user