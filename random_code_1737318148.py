```python
# Welcome to the Enchanted Workshop where magical items are crafted!

def craft_item(item_name):
    print(f"Crafting {item_name}...")
    # Add enchantment to the item
    enchanted_item = f"Enchanted {item_name}"
    return enchanted_item

# List of items to craft
items_to_craft = ["sword", "potion", "ring"]

# Craft each item in the list
for item in items_to_craft:
    enchanted_item = craft_item(item)
    print(f"Crafted: {enchanted_item}")

print("All items have been crafted. Visit us again for more magic!")
```

This enchanted workshop program defines a function to craft magical items and demonstrates crafting a sword, potion, and ring. The loop iterates over the list of items to craft and enchants each one. The program showcases function definition, looping, string formatting, and function return.