```python
# Welcome to the Enchanted Workshop!
# In this workshop, items are magically crafted with the help of enchanted tools.

def craft_item(item_name):
    print(f"Crafting {item_name}...")
    print(f"{item_name} successfully crafted!\n")

# Enchanted tools available in the workshop
enchanted_tools = ["Mystic Hammer", "Wand of Creation", "Sorcerer's Knife"]

# Loop through each enchanted tool to craft a unique item
for tool in enchanted_tools:
    crafted_item = tool.split()[0] + " of Enchantment"
    craft_item(crafted_item)

print("All items have been crafted with enchantment. Visit again for more magical creations!")
```

This Enchanted Workshop script showcases the crafting of magical items using enchanted tools. It features a function to craft items and a loop to create unique items with different enchanted tools each time.