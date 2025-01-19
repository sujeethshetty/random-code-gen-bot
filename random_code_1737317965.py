Certainly! Here's a simple Python program that generates a random password of a specified length using uppercase letters, lowercase letters, and digits:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    
    if length <= 0:
        print("Please enter a valid length for the password.")
    else:
        password = generate_password(length)
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
```

When you run this program, it will