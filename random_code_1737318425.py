Here is a simple Python program that generates a multiplication table for a given number:

```python
def generate_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

# Get user input for the number
try:
    number = int(input("Enter a number to generate its multiplication table: "))
    generate_multiplication_table(number)
except ValueError:
    print("Please enter a valid number.")
```

This program prompts the user to enter a number and then generates and displays the multiplication table for that number up to 10. It includes a function `generate_multiplication