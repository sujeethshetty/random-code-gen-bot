Here is a simple Python program that generates a random quote from a list of quotes:

```python
import random

# List of quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson"
]

def generate_random_quote():
    return random.choice