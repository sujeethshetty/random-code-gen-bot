Certainly! Here's a simple Python program that generates a Fibonacci sequence up to a specified number of terms:

```python
def generate_fibonacci_sequence(num_terms):
    sequence = []
    a, b = 0, 1
    for _ in range(num_terms):
        sequence.append(a)
        a, b = b, a + b
    return sequence

num_terms = 10
fibonacci_sequence = generate_fibonacci_sequence(num_terms)

print(f"Fibonacci Sequence up to {num_terms} terms:")
for term in fibonacci_sequence:
    print(term, end=' ')
```

This program defines a function `generate_fibonacci_sequence` that generates a Fibonacci sequence up to the specified number of terms. It then