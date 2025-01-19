Here is a simple Python program that generates a Fibonacci sequence up to a specified number of terms:

```python
def generate_fibonacci_sequence(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

def main():
    n = int(input("Enter the number of Fibonacci sequence terms to generate: "))
    fibonacci_sequence = generate_fibonacci_sequence(n)
    print("Fibonacci sequence up to", n, "terms:")
    print(fibonacci_sequence)

if __name__ == "__main__":
    main()
```

This program defines a `generate_fibonacci