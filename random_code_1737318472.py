Certainly! Here's a simple Python program that generates and prints a random quote:

```python
import random

def get_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The best way to predict the future is to create it. - Peter Drucker"
    ]
    
    return random.choice(quotes)

def main():
    quote = get_random_quote()