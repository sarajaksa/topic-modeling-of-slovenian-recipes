from bs4 import BeautifulSoup
import pickle
import os

folder = "data"
filename = "ingredients_by_recipe.pickle"

list_of_recipes_files = os.listdir(folder)


def process_ingredient(ing):
    result = [word.get_text() for word in ing.find_all(class_="label-value")]
    result = " ".join(result).lower().strip()
    return result


recipes_ingredients = []
for filename in list_of_recipes_files:
    with open(os.path.join(folder, filename)) as f:
        data = f.readlines()
        data = " ".join(data)
    data_html = BeautifulSoup(data)
    ingredients = data_html.find_all("p", itemprop="recipeIngredient")
    ingredients = [process_ingredient(ing) for ing in ingredients]
    recipes_ingredients.append(ingredients)

with open(filename, "wb") as f:
    pickle.dump(recipes_ingredients, f)
