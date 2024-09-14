"""
Written by: Richard Wakefield
Date: September 14, 2024

This program will convert the .json python data scraped from the web to a .csv file to be used in the excel sheet for the end user.
"""

import pandas as pd

with open('jsonfile.json') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('csvfile.csv', index=False)
