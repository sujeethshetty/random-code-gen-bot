```python
# Haunted Toy Workshop: A program for creating spooky toys

def create_spooky_toy(toy_name):
    return f"A haunted {toy_name} that glows in the dark"

def display_workshop_inventory(toys_list):
    print("Welcome to the Haunted Toy Workshop! Check out our spooky toys:")
    for index, toy in enumerate(toys_list, start=1):
        print(f"{index}. {toy}")

# List of spooky toys in the workshop
spooky_toys = ['creepy doll', 'possessed teddy bear', 'phantom train set']

# Display the inventory of spooky toys
display_workshop_inventory(spooky_toys)

# Create a new spooky toy and add it to the inventory
new_toy = create_spooky_toy("cursed jack-in-the-box")
spooky_toys.append(new_toy)

# Display the updated inventory
display_workshop_inventory(spooky_toys)
```