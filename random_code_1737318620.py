Here is a simple Python program that generates a random quote each time it is run:

```python
import random

def get_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "The best way to predict the future is to create it. - Peter Drucker",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson"
    ]
    
    return random.choice(quotes)

def main():
    print("Here is your random quote