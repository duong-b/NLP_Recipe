import numpy as np
import pandas as pd

from recipe_locations import *   # * means import everything
from utils import get_units
from web_scraping import url_to_text_food_dot_com


units = get_units()
df = url_to_text_food_dot_com(food_dot_com_url[0])
print(df)

