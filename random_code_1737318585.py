Here is a simple Python program that generates a random math quiz for users to solve:

```python
import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    question = f"What is {num1} {operator} {num2}? "
    
    return question, answer

def main():
    print("Welcome to the Math Quiz!")
    score = 0
    num_questions