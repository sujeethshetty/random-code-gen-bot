Below is a simple Python program that generates a random password of a specified length using a combination of uppercase letters, lowercase letters, and numbers:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password you want to generate: "))
    password = generate_password(length)
    print("Your random password is:", password)

if __name__ == "__main__":
    main()
```

When you run this program, it will prompt you to enter the length of the password you want to generate. After entering the length