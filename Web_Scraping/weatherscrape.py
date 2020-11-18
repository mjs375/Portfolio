"""National Weather Service: Webscraper
    - Scrapes 7-day forecast data from NWS
-> Tutorial Source: https://www.dataquest.io/blog/web-scraping-tutorial-python/
  - v 1.0) Program functions successfully, + export data as csv feature (prompts)
"""

from bs4 import BeautifulSoup # python3 -m pip install beautifulsoup4
from datetime import datetime
import os
import pandas as pd # pip install pandas
import re
import requests # python3 -m pip install requests
import sys
import time

os.system('clear')


url = "https://forecast.weather.gov/MapClick.php?lat=40.8535&lon=-74.8288#.X7VlUhNKjOQ"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
period_tags = seven_day.select(".tombstone-container .period-name") # Select all items w/ class 'tombstone-container' inside 'seven_day'

# # # Now use list comprehension to get each day's data:
periods = [period_tag.get_text() for period_tag in period_tags]
print(periods) #['Tonight', 'Thursday', 'ThursdayNight',...]
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

# # # At this point we have multiple lists of data relating to the 7-day forecast:
print(short_descs)
print(temps)
print(descs)


# # # Combining our Data into a Pandas Dataframe:
    # a Dataframe object (a class instance) can store tabular data , in the form of a Dictionary (key = column; each list will become values in the columns)
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs,
})
print("\n\n",weather)

# # # Now for some ANALYSIS:
    #
print("XXXX",weather["temp"])
temp_nums = weather["temp"].str.extract("([0-9]+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
print(temp_nums)



# Mean of all Highs/Lows:
print("Mean temp:",weather["temp_num"].mean()) #
# Select only the nights:
is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night # Col says whether is night or not
# print(is_night)


# # # Export all collected data to a .CSV
answer = input("Export collected data to .csv file? (y/n)\n>>> ")
if "y" in answer.lower():
    print("Exporting...")
else: # NO:
    confirm = ("Data will not be exported. Are you sure you want to finish without exporting? (y/n)\n")
    if "y" in confirm.lower():
        sys.exit("Data not exported. Program over.")
    if "n" in confirm.lower():
        print("Exporting...")
time.sleep(2)
# # # Now to export the data as .CSV:
filename = datetime.today()
try:
    weather.to_csv(f'{filename}_forecast.csv')
    print("File successfully exported")
except:
    print("Issue in exporting file...")
    
    
    
# # # # # # # # # # # # # # # #
