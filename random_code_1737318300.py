Here is a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password: "))
    
    if password_length <= 0:
        print("Password length should be a positive integer.")
        return
    
    password = generate_password(password_length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
```

In this program:
- The `generate_password` function generates a random password of the specified length using a combination of