Certainly! Here's a spooky Python program set in a haunted toy workshop:

```python
def create_haunted_toys(num_toys):
    haunted_toys = []
    for i in range(1, num_toys + 1):
        toy_name = f"Haunted Toy {i}"
        haunted_toys.append(toy_name)
    return haunted_toys

def play_with_toys(toy_list):
    for toy in toy_list:
        print(f"Playing with {toy}...")
    print("Oh no, the toys are moving on their own! 👻")

# Welcome to the Haunted Toy Workshop!
print("Welcome to the Haunted Toy Workshop! 🧸👻")

# Create some haunted toys
num_toys = 3
haunted_toys = create_haunted_toys(num_toys)

# Display the haunted toys
print("Behold the haunted toys in the workshop:")
for toy in haunted_toys:
    print(toy)

# Time to play with the toys
play_with_toys(haunted_toys)
```

In this program, we create a list of haunted toys in a workshop using a function and loop. Then, we simulate playing with the toys, only to discover that they are haunted and start moving on their own. This program showcases the use of functions, loops, and string formatting in Python to create a fun and whimsical experience.