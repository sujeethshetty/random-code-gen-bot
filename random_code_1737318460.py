Here is a simple Python program that generates a random maze using ASCII characters. It includes functions, variables, loops, and conditional statements:

```python
import random

def generate_maze(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]

    for i in range(1, height-1):
        for j in range(1, width-1):
            if random.random() < 0.7:  # 70% chance of empty space
                maze[i][j] = ' '
    
    maze[1][1] = 'S'  # Start point
    maze[height-2][width-2] = 'E'  # End point