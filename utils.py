import pandas as pd
import numpy as np


def get_units():
    with open("units.txt", "r") as f:   # open any text file as f. Argument "r" makes it read-only
        return f.read().splitlines()    # f.read.splitlines  returns every line into a list item,



