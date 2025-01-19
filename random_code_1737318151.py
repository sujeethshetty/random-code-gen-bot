Here is a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    
    if length < 1:
        print("Password length should be at least 1.")
    else:
        password = generate_password(length)
        print(f"Your random password is: {password}")

if __name__ == "__main__":
    main()
```

You can run this program in your Python environment by copying and past