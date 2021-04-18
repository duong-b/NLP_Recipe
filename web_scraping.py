# web scraping
import requests
from bs4 import BeautifulSoup
import pickle
import pandas as pd
import numpy as np
import re
import lxml


# Scraping recipes from Food.com
def url_to_text_food_dot_com(url):
    page = requests.get(url)# convert webpage into text
    page.encoding = "utf-8"
    page = page.text
    soup = BeautifulSoup(page, "lxml")  # create the soup

    quantity = []
    unit = []
    ingredients = []

    ingredients_unparsed = soup.find_all('div', attrs={'class': 'recipe-ingredients__ingredient'})
    for item in ingredients_unparsed:
        #       print(item)
        try:
            #         item_full = item.get_text()
            quantity.append(float(item.find(class_='recipe-ingredients__ingredient-quantity').text))
            unit.append(item.find(class_='recipe-ingredients__ingredient-part').text.strip())
            ingredients.append(item.find('a').text)
        except AttributeError:
            ingredients.append('NA')

    # Fix the item that does not follow the pattern
    #     x = unit[2].split('    ')
    #     unit[2] = x[0]
    #     ingredients[2] = x[1]

    # print(f"{quantity} \n {unit} \n {ingredients}")

    #  Make a dataframe
    csv = {"Quantity": np.array(quantity), "Units": unit, "Ingredients": ingredients}
    df = pd.DataFrame(data=csv)
    df.attrs['url'] = url
    # print(df)
    # print(df.attrs)
    return df


# Scraping from AllRecipes.com
def url_to_text_allrecipe(url):
    page = requests.get(url).text  # convert webpage into text
    soup = BeautifulSoup(page, "lxml")  # create the soup

    # Within the classes contained 'recipe-ingredients__ingredient', find all'div'
    #     ingredients_unparsed = soup.find_all(class_="checkbox-list")
    ingredients_unparsed = soup.select('[for^="recipe-ingredients-label"]')
    #     ingredients_unparsed = soup.find_all(re.compile("^recipe-ingredients-label"))
    #     print(ingredients_unparsed)

    quantity = []
    units = []
    ingredients = []

    for item in ingredients_unparsed:
        item_full = item.find_all(class_="checkbox-list-input")[0]
        quantity.append(item_full.get("data-init-quantity"))
        units.append(item_full.get("data-unit"))
        ingredients.append(item_full.get("data-ingredient"))

    # print(f"{quantity}\n{units}\n{ingredients}")

    csv = {"Quantity": quantity, "Units": units, "Ingredients": ingredients}
    df = pd.DataFrame(data=csv)
    df.attrs['url'] = url
    # print(df)
    # print(df.attrs)
    return df

