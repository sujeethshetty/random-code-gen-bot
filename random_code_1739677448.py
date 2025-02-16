```python
# Welcome to the Galactic Cooking Showdown!
# In this competition, alien chefs battle to create the most delicious dish in the galaxy.

def prepare_ingredients(ingredient_list):
    prepared_ingredients = []
    for ingredient in ingredient_list:
        prepared_ingredients.append("prepared " + ingredient)
    return prepared_ingredients

def cook_dish(prepared_ingredients):
    dish = ""
    for ingredient in prepared_ingredients:
        dish += ingredient + ", "
    return dish + "and a pinch of stardust"

ingredient_list = ["moonberries", "nebula noodles", "plutonian peppers"]

print("Let's see what our contestants are cooking today!")
print("-------")

for i in range(3):
    chef_name = "Chef " + str(i+1)
    print(chef_name + " is preparing their dish...")
    
    prepared_ingredients = prepare_ingredients(ingredient_list)
    
    print(chef_name + " has finished preparing the ingredients.")
    print(chef_name + " is now cooking...")
    
    final_dish = cook_dish(prepared_ingredients)
    
    print(chef_name + " presents: " + final_dish)
    print("-------")

print("The Galactic Cooking Showdown results are in! And the winner is...")
# Add your own twist by implementing a judging mechanism based on dish tastiness or creativity!
```