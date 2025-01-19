Here's a simple Python program that generates and prints a random quote each time it is run:

```python
import random

def get_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "In the middle of every difficulty lies opportunity. - Albert Einstein",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson"
    ]
    
    return random.choice(quotes)

def main():
    print("Here is a random quote