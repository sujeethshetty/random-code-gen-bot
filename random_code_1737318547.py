Here is a simple Python program that generates a random multiplication quiz for the user to solve:

```python
import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 * num2
    return num1, num2, answer

def main():
    print("Welcome to the Multiplication Quiz!")
    score = 0
    num_questions = 5

    for _ in range(num_questions):
        num1, num2, answer = generate_question()
        user_answer = input(f"What is {num1} * {num2}? ")

        if user_answer.isdigit() and int(user_answer) == answer: