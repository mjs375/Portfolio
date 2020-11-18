""" National Weather Service: Webscrape
    - Retrieves 1 day of projected forecast from the 7-day forecast. See 'weatherscrape.py' for a more in-depth program.
Usage: python3 weatherscrapesimple.py [url]
"""

import os
import time
import requests # make the web request
from bs4 import BeautifulSoup # an HTML parser (extract certain content)
import sys

# TODO: prompt for URL using input()/sys.argv


"""
Use your Browser's Developer tools to Inspect the source-code (HTML):
    - Right-click > Inspect
    - TIP: r-click > Inspect (again) on a specific area to see that content's source-code.
Zooming in on the 7'day forecast, we isolate HTML we'll need to find:
    - id = "seven-day-forecase" (contains all days)
    - class = "tombstone container" (contains each day)
"""


url = "https://forecast.weather.gov/MapClick.php?lat=40.8535&lon=-74.8288#.X7VlUhNKjOQ"

page = requests.get(url)
    # TODO: check that URL is valid
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container") # a list
tonight = forecast_items[0]
# print(tonight.prettify())

"""
Each item in forecast_items contains 4 things:
    name, description, short_description, low_temp
"""
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)
img = tonight.find("img")
desc = img['title']
print(desc)






#
