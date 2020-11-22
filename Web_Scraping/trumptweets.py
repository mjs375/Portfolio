"""
Scrapes Trump Tweets from an archive that houses all his deleted Tweets.
TODO: 
  - get pieces of data: tweet, timestamp, &c.
  - add MechanicalSoup capabilities to go to page 1, 2, 3... to scrape more than 50 (loop).
  - export to CSV
"""


import requests
from bs4 import BeautifulSoup

url = "https://projects.propublica.org/politwoops/user/realDonaldTrump"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

tweets = soup.find_all('p', class_='tweet-text')
for tweet in tweets:
    print(tweet.text, '\n')
