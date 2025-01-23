```python
# Welcome to the Magical Cooking Demonstration!
# Today, we will show you the enchanted recipe for 'Sparkling Potion Soup'!

def create_ingredient(name):
    return {'name': name, 'quantity': 0}

def add_ingredient(ingredients, name, quantity):
    for ingredient in ingredients:
        if ingredient['name'] == name:
            ingredient['quantity'] += quantity
            return ingredients
    ingredients.append({'name': name, 'quantity': quantity})
    return ingredients

def mix_ingredients(ingredients):
    for ingredient in ingredients:
        print(f"Mixing {ingredient['quantity']} units of {ingredient['name']}...")
    print("Voilà! The potion soup is ready! 🌟✨🍲")

# Let's gather the magical ingredients
ingredients_list = []
ingredients_list = add_ingredient(ingredients_list, 'Fairy Dust', 3)
ingredients_list = add_ingredient(ingredients_list, 'Dragon Scale Powder', 1)
ingredients_list = add_ingredient(ingredients_list, 'Moonlight Essence', 2)

# Display the gathered ingredients
print("Ingredients for Sparkling Potion Soup:")
for ingredient in ingredients_list:
    print(f"{ingredient['quantity']} units of {ingredient['name']}")

# Time to mix the ingredients and create the magical potion
print("\nPreparing the Sparkling Potion Soup...")
mix_ingredients(ingredients_list)
```

This program showcases a magical cooking demonstration where