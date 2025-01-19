Here's a simple Python program that generates and prints a random quote each time it is run:

```python
import random

def get_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In the middle of every difficulty lies opportunity. - Albert Einstein",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. - Confucius"
    ]
    return random.choice(quotes)

def main():
    print("Welcome to the Random Quote