import numpy as np
import pandas as pd

from recipe_locations import *
from web_scraping import *
from utils import replace_na_row
from fractions import Fraction

# units = get_units()
df = url_to_text_food_dot_com(food_dot_com_url[0])
ingredient_na = replace_na_row(df)
print(df)
# print(df.Ingredients)

