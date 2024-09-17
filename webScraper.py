"""
Written by: Richard Wakefield
Date: September 14, 2024

This program scrapes the web for the project component prices and outputs them to a .json file to be handled by pandas.
"""

import json
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)

# To learn webscraping, learn Beautiful Soup (bs4), Selenium, or Scrapy.
