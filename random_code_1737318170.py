Here is a simple Python program that generates a random password of a specified length with a combination of lowercase letters, uppercase letters, and digits:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    
    if length <= 0:
        print("Length must be greater than 0.")
    else:
        password = generate_password(length)
        print("Generated password:", password)

if __name__ == "__main__":
    main()
```

In this program:
- We import the `random