```python
# Welcome to the Enchanted Workshop!
# In this magical workshop, objects come to life when given special enchantments.

def enchant_object(object_name, enchantment):
    return f"{enchantment.capitalize()} {object_name}"

workshop_inventory = ["wand", "mirror", "book", "ring"]
enchantments = ["glowing", "whispering", "sparkling", "shimmering"]

print("The Enchanted Workshop is ready to enchant objects!")

for item in workshop_inventory:
    enchantment = enchantments.pop(0) if enchantments else "mysterious"
    enchanted_item = enchant_object(item, enchantment)
    print(f"{item.capitalize()} is now {enchanted_item}!")

print("All objects in the workshop have been enchanted. Come back soon!")
```

This whimsical Python program simulates an enchanted workshop where ordinary objects are given magical enchantments. The 'enchant_object' function combines an object's name with an enchantment, creating a magical transformation. The workshop's inventory is enchanted one by one, using a loop to iterate through each object and assign a unique enchantment. The program showcases the fun of magical transformations and the concept of enchantments in a creative setting.