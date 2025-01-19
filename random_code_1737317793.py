Certainly! Here's a simple Python program that generates a random password of a specified length using letters, numbers, and special characters:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password you want to generate: "))
    password = generate_password(length)
    print(f"Your random password is: {password}")

if __name__ == "__main__":
    main()
```

In this program:
- We import the `random` and `string` modules to generate random characters for the