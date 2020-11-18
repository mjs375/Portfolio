""" NATIONAL WEATHER SERVICE WEBSCRAPER
- Scraper: BeautifulSoup
- Analysis: Pandas library

Usage: $ python3 webscrapepractice.py
"""
import os
import time
import requests # make the web request
from bs4 import BeautifulSoup # an HTML parser (extract certain content)
os.system('clear') # clears the console screen for clarity
url = "http://dataquestio.github.io/web-scraping-pages/simple.html"
page = requests.get(url)
    # <Response [200]> :means page downloaded OK
# print(page.content) # an ugly printout of the HTML

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify()) # much prettier printout
#print("\n")
print(list(soup.children))
print("\n")
print([type(item) for item in list(soup.children)])
print("\n")
# Select the html tag [2] and its children
html = list(soup.children)[2]
# Call on the children property again
print(list(html.children))
# Now we want the body (of <head> and <body> given by prior step):
body = list(html.children)[3]
print("\n")
print(list(body.children))
# Now we are in the <body>, and need 1 last child (<p>):
p = list(body.children)[1]
print(p.get_text()) # Get the raw content of the p tag inside body inside ... ...
"""
The above method found a series of nested children elements,
    using indexing to choose which child-nest to explore next.
To find all instances of a single tag (e.g. <p>), we don't have to
    manually navigate each child element, we can just...:
"""
soup.find('p') # will just find the FIRST INSTANCE of a tag
#
soup.find_all('p') # returns a list of all p-tags
    # Either LOOP thru, or INDEX to get a particular instance of <p>
print(soup.find_all('p')[0].get_text())
