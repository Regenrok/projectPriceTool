"""
Written by: Richard Wakefield
Date: September 14, 2024

This program scrapes the web for the project component prices and outputs them to a .json file to be handled by pandas.
"""

from urllib.request import Request, urlopen
import re

url = "https://www.fcpeuro.com/BMW-parts/323Ci/?year=2000&m=20&e=177&t=6&b=9&d=65&v="

req = Request(url, headers = {'User-Agent': 'Chrome/129.0.0.0'})

page = urlopen(req).read().decode("utf-8")

pattern = 'Sachs 556873KT.*?data-price=".*?"'

match = re.search(pattern, page)

print(match)
# To learn webscraping, learn Beautiful Soup (bs4), Selenium, or Scrapy.
