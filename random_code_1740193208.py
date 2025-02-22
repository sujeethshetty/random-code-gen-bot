```python
def magical_paintbrush_adventure():
    canvas = [[' ' for _ in range(10)] for _ in range(10)]  # Create a 10x10 canvas

    def paint(x, y, color):
        if 0 <= x < 10 and 0 <= y < 10:
            canvas[y][x] = color

    print("Let's embark on a magical paintbrush escapade!")
    
    while True:
        print("\nCurrent Canvas:")
        for row in canvas:
            print(' '.join(row))
        
        x = int(input("Enter x coordinate (0-9): "))
        y = int(input("Enter y coordinate (0-9): ")
        color = input("Enter color to paint with: ")

        paint(x, y, color)

        cont = input("Do you want to continue painting? (y/n): ")
        if cont.lower() != 'y':
            break

    print("\nFinal Masterpiece:")
    for row in canvas:
        print(' '.join(row))

magical_paintbrush_adventure()
``` 

This program allows you to create your masterpiece on a 10x10 canvas using a magical paintbrush. You can choose the coordinates and color to paint with, seeing your creation unfold interactively.