Here is a simple Python program that generates a random motivational quote each time it is run:

```python
import random

def get_motivational_quote():
    quotes = [
        "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
        "The only limit to our realization of tomorrow will be our doubts of today.",
        "Believe you can and you're halfway there.",
        "The best way to predict the future is to create it.",
        "Don't watch the clock; do what it does. Keep going.",
        "Your time is limited, don't waste it living someone else's life."
    ]

    return random.choice(quotes)