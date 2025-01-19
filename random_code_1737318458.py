Certainly! Here's a simple Python program that calculates the factorial of a number input by the user:

```python
# Function to calculate the factorial of a number
def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

# Main program
if __name__ == "__main__":
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = calculate_factorial(num)
            print(f"The factorial of {num} is: {result}")
    except ValueError:
        print("Please enter