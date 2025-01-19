Here is a simple Python program that generates a random inspirational quote every time you run it:

```python
import random

# List of inspirational quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson"
]

def generate_inspiration():
    # Generate a random index to select a quote
    index = random