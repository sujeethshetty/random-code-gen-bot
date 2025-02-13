```python
# Welcome to the Galactic Cooking Showdown!
# In this competition, alien chefs prepare dishes from all corners of the universe.

def prepare_dish(ingredient):
    return ingredient + " sautéed with stardust and seasoned with cosmic spices"

contestants = ["Zorblax", "Glipgorp", "Xandar", "Nebulon"]
dish_ingredients = ["Neptunian squid", "Plutonian mushrooms", "Saturnian truffles", "Martian herbs"]

print("Let the Galactic Cooking Showdown begin!\n")

for chef in contestants:
    print(f"{chef} is preparing an out-of-this-world dish...")
    dish_ingredient = dish_ingredients.pop(0)
    prepared_dish = prepare_dish(dish_ingredient)
    print(f"{chef} has prepared: {prepared_dish}\n")

print("Tasting time! Let's see whose dish reigns supreme across the galaxy!")
```
This program simulates a Galactic Cooking Showdown where alien chefs create dishes using exotic ingredients. Each chef prepares a unique dish with an ingredient, showcasing a whimsical cooking competition theme.