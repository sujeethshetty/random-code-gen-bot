```python
# Welcome to the Enchanted Workshop where magical items are crafted!
# This program will help you create a personalized enchanted item.

def enchant_item(material, power_level):
    enchanted_item = ""
    for letter in material:
        enchanted_item += chr(ord(letter) + power_level)
    return enchanted_item

workshop_material = input("Enter a material for your enchanted item: ")
workshop_power = int(input("Enter the power level for the enchantment (1-5): "))

if 1 <= workshop_power <= 5:
    crafted_item = enchant_item(workshop_material, workshop_power)
    print(f"Behold! You have created the enchanted '{crafted_item}' in the Enchanted Workshop!")
else:
    print("Invalid power level. Please choose a power level between 1 and 5.")
```

This enchanted workshop program allows you to input a material and a power level for an enchantment, which then transforms the material into a magical item by shifting the ASCII values of its characters. The program ensures that the power level is within the specified range before enchanting the item.