import pandas as pd
import numpy as np
from web_scraping import url_to_text_food_dot_com


def get_units():
    with open("units.txt", "r") as f:  # open any text file as f. Argument "r" makes it read-only
        return f.read().splitlines()  # f.read.splitlines  returns every line into a list item,

# The below function works for Food.com recipes
def replace_na_row(df):
    # df.index is to look for the index, make a list of index that satisfies the condition
    index = df[df['Ingredients'].isin(['NA'])].index.tolist()
    for i in index:
        result = df.Units[i].split('    ', 2)
        df.at[i, 'Units'] = result[0]  # df.at is used to change texts at certain row
        df.at[i, 'Ingredients'] = result[1]
    return df

