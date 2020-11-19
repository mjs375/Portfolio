"""National Weather Service: Webscraper
    - Scrapes 7-day forecast data from NWS.
    - Tutorial Source: https://www.dataquest.io/blog/web-scraping-tutorial-python/
    -> I added user prompts, csv export option, &c. (Depending on your needs, you can remove the user prompts to make a fully automatic, 1-command program.)
"""

from bs4 import BeautifulSoup # python3 -m pip install beautifulsoup4
from datetime import datetime
import os
import pandas as pd # pip install pandas
import re
import requests # python3 -m pip install requests
import sys
import time
from urllib.request import HTTPError, URLError


def scrape_weather():
    ### Clear the screen for clarity:
    os.system('clear')
    #
    url = "https://forecast.weather.gov/MapClick.php?lat=40.8535&lon=-74.8288#.X7VlUhNKjOQ"
    ### Attempt to request the webpage of 'url':
    try:
        page = requests.get(url)
    except HTTPError as e:
        sys.exit("HTTP error")
    except URLError as e:
        sys.exit("Server not found.")
    ### Parse HTML into BeautifulSoup object:
    soup = BeautifulSoup(page.content, 'html.parser')
    ### Find HTML code-block specific to our desired content:
    seven_day = soup.find(id="seven-day-forecast")
    ### Select the inner HTML of our block with the data itself:
    period_tags = seven_day.select(".tombstone-container .period-name")
    #
    #
    #
    ### Now use list comprehension to get each day's 4 pieces of data:
    periods = [period_tag.get_text() for period_tag in period_tags]
    short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
    temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
    descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
    ### At this point we have multiple lists of data relating to the 7-day forecast:
    print(periods)
    print(short_descs)
    print(temps)
    print(descs)


    ### Combining our Data into a Pandas Dataframe:
        # a Dataframe object (a class instance) can store tabular data , in the form of a Dictionary (key = column; each list will become values in the columns)
    weather = pd.DataFrame({
        "period": periods,
        "short_desc": short_descs,
        "temp": temps,
        "desc": descs,
    })
    print("\n\n",weather) # prints the Dataset table
    #
    #
    #
    ### Now for some ANALYSIS:
    temp_nums = weather["temp"].str.extract("([0-9]+)", expand=False) # isolate the digits in the temp string ("Low: 40ºF")
    weather["temp_num"] = temp_nums.astype('int') # cast as type 'int'
    print(temp_nums)
    #
    #
    # Mean of all Highs/Lows:
    print("Mean temp:",weather["temp_num"].mean()) #
    # Select only the nights:
    is_night = weather["temp"].str.contains("Low")
    weather["is_night"] = is_night # New added col says whether row is night or not
    # print(is_night)
    #
    #
    #
    time.sleep(2)
    #
    #
    #




    ### Export all collected data to a .CSV
       ### Prompts for user input: do they want a .csv file?
    check = False
    answer = input("Export collected data to .csv file? (y/n)\n>>> ")
    while check == False:
        if "y" in answer.lower():
            time.sleep(1)
            print("Exporting...")
            check = True # exit loop
        else: # NO:
            confirm = input("Data will not be exported. Are you sure you want to finish without exporting? (y/n)\n>>> ")
            if "y" in confirm.lower():
                time.sleep(1)
                sys.exit("Data not exported. Program over.")
            if "n" in confirm.lower():
                time.sleep(1)
                print("Exporting...")
                check = True
    #
    #
    #
    time.sleep(1)
    # # # Now to export the data as .CSV:
    filename = datetime.now()
    filename = str(filename.strftime("%m/%d/%Y")).replace("/","-") + "_forecast"
    filename = input(f"Enter a filename or press enter for default ('{filename}.csv'): ")
            \ or filename
    try:
        weather.to_csv(f'{filename}.csv', sep="|", index=False)
        print("Successful export.")
    except:
        print("Error in exporting file...")
    sys.exit()
#
# #
# # #
# #
#

#TODO: allow url as argv
#
scrape_weather() # RUN THE PROGRAM!!!
