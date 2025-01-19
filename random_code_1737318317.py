Here is a random Python program that generates a simple multiplication table for a given number:

```python
def generate_multiplication_table(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

def main():
    user_input = input("Enter a number to generate its multiplication table: ")
    
    try:
        number = int(user_input)
        generate_multiplication_table(number)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
```

This program prompts the user to enter a number and then generates the multiplication table for that number from 1 to 10. It demonstrates the