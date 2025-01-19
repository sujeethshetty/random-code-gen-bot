Here's a simple Python program that calculates the average of a list of numbers input by the user:

```python
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

def main():
    numbers = []
    n = int(input("Enter the number of elements: "))
    
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    
    avg = calculate_average(numbers)
    
    print(f"The average of the numbers is: {avg}")

if __name__ == "__main__":
    main()
```

In this program, the `calculate_average` function calculates the average of the numbers in a list.