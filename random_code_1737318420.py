Here is a simple Python program that generates a random password based on the user's input for password length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password you want to generate: "))
    
    if length <= 0:
        print("Invalid password length. Please enter a positive number.")
    else:
        password = generate_password(length)
        print(f"Your random password of length {length} is: {password}")

if __name__ == "__main__":
    main()