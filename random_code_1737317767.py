Sure, here is a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password you want to generate: "))
    
    if password_length <= 0:
        print("Password length should be greater than 0.")
    else:
        random_password = generate_random_password(password_length)
        print(f"Randomly generated password of length {password_length}: {random_password}")

if __name__ == "__main__":