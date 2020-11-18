## W E B _ S C R A P I N G _ I N _ P Y T H O N
- Many websites have fantastic datasets that are publicly available, but not all are made accessible via CSV download, or API-link. So what's left to try, besides mass copy-&-pasting?
- **Rules:** *webscraping is the same as your going on to a website and making requests... so if you scrape 1000 times in a minute, that's expensive!*
  - *check Terms and Conditions of website to see if webscraping is permitted*
  - *cache or download data you need, so that next analysis, you don't need to download it again (or only download the latest data, not the entire set again)*
  - *build pauses into the program (```time.sleep()```) to not overwhelm the server*
  
### Components of a Web Page
- **HTML**: *main content/structure of the page*
- **CSS**: *styling of the page content*
- **Javascript**: *added interactivity to webpages (forms, buttons)*
- Images
  - *our browser receives these main files types (plus others), and combines them into a rendered page. With webscraping we are interested in __content__, so look to the __HTML__.*

- **Web Scraper Libraries**:
  - [Requests Library](#python's-requests-library)
  - from urlllib.request import urlopen
  - import BeautifulSoup
  - import MechanicalSoup

### Gather the HTML source-code in a string:
```python
from urllib.request import urlopen # Tools for working with URLs (urlopen() can open a URL within a program)

url = "http://website.com/you/wish/to/scrape" # website URL to be opened for scraping

page = urlopen(url) # opens the webpage, returns an 'HTTPResponse object (e.g. 'http.client.HTTPResponse object at 0x105fef820')

html_bytes = page.read() # .read() returns a sequence of bytes

html = html_bytes.decode("utf-8") # decodes bytes into a string, using UTF-8

print(html) # 'html' now contains all the HTML source code in a string
```

<hr> 

### Simple Method of Extraction:
- **String Methods**: *using .find() and string slicing syntax, you can pull the index range of HTML between 2 tags, e.g. <title>...</title>. This is a very simple method vulnerable to many failings: it can only find the first instance, if '<title>' is actually '<title id="hdg">' it won't find it, &c.*
  - ```.find()```: *searches a string for the first instance of the string-pattern*
```python
    # <title>Poseidon</title>
title_index = html.find("<title>") # get the index of the '<' in '<title>'
start_index = title_index + len("<title>") # get the index of the first letter of the actual title, "'P'oseidon"
end_index = html.find("</title>") # repeat for close tag
title = html[start_index:end_index]
print(title) # "Poseidon"
```
   

### Regular Expressions – Extracting Data between HTML tags (manually):

### REGEX Special Characters, Functions & Syntax
- ```*```: *0+ occurrences of whatever preceded*
- ```.```: *1+ occurrences of whatever preceded*
  - ```.*```: *matches any character any number of times*
  - ```.*?```: *non-greedy matching pattern (finds the shortest possible match, rather than the longest* 

### REGEX Functions:
  - ```import re```: *Regex module must be imported to use*
- ```re.findall(pattern, string,)```: *find any and all matches of the pattern in a string, returning a list of all matches/*
  - ```re.findall("ab*c", "abcac")``` => ['abc', 'ac']
- ```re.search()```: *returns a 'match object' of all possible matches (even matches inside matches)*
  - ```x = matches.group()```: *gives the first and most inclusive result (unpacks the match object)*
- ```re.sub(pattern, replace_text, string,)```: *replace text in a string that matches a regular expression with new text (behaves akin to string.replace()). Example ```string = "Everything is <replaced> if it's in <tags>."```*
  - ```print(re.sub("<.*>", "!!!", string))``` => ```Everything is !!!.``` *This happens because Python's regular expressions are 'greedy'– they try to find the longest possible match.*
  - ```print(re.sub("<.*?>", "!!!", string))``` => ```Everything is !!! if it's in !!!.```

### HTML Regex
- ```match_result = re.search(pattern, html, re.IGNORECASE)```
  - ```tag_and_contents = match_results.group()```
- ```pattern = "<tag.*?>.*?</tag.*?>"``` => ```<TITLE >Profile: Dionysus</title  / >```: *a sample regex for capturing the inner contents of any <tag>contents</tag> substring in the html-string. (Use re.IGNORECASE as a 3rd-argument.)*
  - ```"<tag.*?>"```: *matches an opening tag, from '<tag' until the first '>', e.g. "<div id='ex'>".*
  - ```.*?```: *non-greedily matches all text after '<tag...>', up until first instance of...*
  - ```</title.*?>```: *the closing tag, e.g. '</TITLE >'.*
- ```re.sub("<.*?>", "", title)```: *removes the tags themselves from the substring.*

<hr>

### Beautiful Soup: HTML Scraper
- a parser designed specifically for HTML pages
  - to install: ```$ python3 -m pip install beautifulsoup4```
  - see details (name, version, license, &c.): ```$ python3 -m pip show beautifulsoup4```
- Limitations: *BeautifulSoup can't work with HTML forms (e.g. search a website for some query, then scraping results). If the HTML is extremely complex, idiosyncratic or poorly-written, it may fail you.*

```python
from bs4 import BeautifulSoup
from urllib.request import urlopen
#
url = "http://website.com/path/name"
page = urlopen(url) # open the URL
html = page.read().decode("utf-8") # converts HTML into a string
soup = BeautifulSoup(html, "html-parser") # creates a BeautifulSoup object (html.parser in Python's built-in HTML parser)
```
#### Using a BeautifulSoup Object
- ```soup.title``` => "<title>Google</title>": *certain tags in HTML docs can be accessed by properties of the Tag Object (note: Beautiful Soup automatically cleans up poorly-written HTML, removing extra spaces, etc.).*
  - ```soup.title.string``` => "Google": *access just the content, not '<tag>content</tag>'*
- ```text = soup.get_text()```: *extracts ALL text from the document, removing ALL HTML tags*
  - ```text.replace("\n","")```: *remove the newlines (lots of blank space in 'text')*
  - ```text.find()```: *this string method was clunky with all the HTML still in, but afterwards, it may be easiest (and simplest) to use it on the raw text content to find what you need* 
- ```soup.find_all("tag")```: *find & return a list of all instances (not strings) of a particular tag*
  - ```soup.find_all('img')``` => ```[<img src="... .jpg"/>, <img src="... .jpg"\>]```
  - 
  - ```image1, image2 = soup.find_all('img')```: *assign each instance of the Tag Object to a variable*
    - ```image1.name``` => 'img' : *each Tag Object has a .name property, which returns a string containing the HTML tag type*
    - ```image["attribute"]```: ```image["src"]``` => '/static/picture.jpg'
    - ```soup.find_all("img", src="/static/picture.jpg")```

### Mechanical Soup: Interact with HTML Forms
- Sometimes you need to request the contents of a webpage (via a form/search query, a button click) before scraping results. MechanicalSoup installs a 'headless browser', i.e. a web browser with no GUI. The browser is instead controlled programmatically via Python.
  - To install: ```$ python3 -m pip install MechanicalSoup```
  - View Details: ```$ python3 -m pip show mechanicalsoup```
```python
  import mechanicalsoup
  browser = mechanicalsoup.Browser() # represents the headless web browser
  url = "http://website.com/page"
  page = browser.get(url) # request a page from the Internet by passing a URL to method .get()
    # page => <Response [200]> (Page is a Response Object from the URL request: 200 OK, 404 Does Not Exist, 500 Server Error)
    # MechanicalSoup uses Beautiful Soup to parse HTML from the request: 
  type(page.soup) # <class 'bs4.BeautifulSoup'> ('Page' has a .soup attribute that represents a BeautifulSoup object).
  page.soup # View the HTML by inspecting the .soup attribute
```
  - Submit a Form with Mechanical Soup: *may need to enter a search query, submit login credentials, etc. before scraping web content. The important code now is inside ```<form>...</form>```, aka a username field, a password field (both <input>s), and a submit button*
    - Note: many hackers use automated programs to try to brute-force login by rapidly trying usernames/passwords. This is illegal, and websites will lock you out anyway if you make too many failed requests.
- 1. **Interact with a Form**: e.g. fill out username/password fields to login
```python
import mechanicalsoup
  # Step 1. 
browser = mechanicalsoup.Browser() # create a headless browser instance
url = "http://website.com/login" # website to visit (login page)
login_page = browser.get(url) # request URL/page
login_html = login_page.soup # get the HTML via the .soup attribute, assign to variable
  # Step 2. 
form = login_html.select("form")[0] # select all <form> elements on page, get element index 0
form.select("input")[0]["value"] = "username" # use Python to interact with the headless browser,
form.select("input")[1]["value"] = "password" # entering username/password into the fields.
  # Step 3.
profiles_page = browser.submit(form, login_page.url) # submit the filled out form (submit both the 'form' object and the URL of the login_page)
profiles_page.url # check => "http://website.com/welcome" # WE ARE IN! a 2nd url variable, further in
```
- **2. Now that we 'are in', let's scrape some data**: e.g. the URL for each link on the welcome page
```python
  # ^^cont. from above^^
links = profiles_page.soup.select("a") # get all <a> tags on the page
base_url = "http://website.com" # concatenate to later relative URLs to get the full link...
for link in links: # iterate over each link, get the href attribute:
  address = basae_url + link["href"] # http://website.com + /profiles/aphrodite
  text = link.text
  print(f"{text}: {address}") # e.g. Aphrodite: /profiles/aphrodite 
```
- **3. Interact with Websites in Real Time**: *repeated webscraping/updating*
  - *What if you need to collect data in real-time/multiple times? You don't want to sit and click 'refresh'! The example website includes a button to roll a dice, as well as a timestamp.*
    - 1. Examine the HTML page source-code in a browser, using 'Inspect Element/View Page Source'. What HTML encloses the content you're looking for? => "<h2 id="result">4</h2>". Let's open the dice page, scrape the results, and print it to the console.
```python
import mechanicalsoup
import time #time.sleep(seconds) => represents the amount of time to sleep (pause running code)

browser - mechanicalsoup.Browser() # open headless browser instance
for i in range(4): # we want to roll the dice 4 times total
    page = browser.get("http://olympus.realpython.org/dice") # request the URL page
    tag = page.soup.select("#result")[0] # get the first instance of "#result" (it's an id so there's only 1 anyway) using BeautifulSoup object's .select() method
    result = tag.text # get the 'raw content' inside that tag
    print(f"The result of the dice roll is: {result}")
    if i < 3: # (no need to wait 10sec after the last loop!)
      time.sleep(10) # tell the program to wait 10 sec between iterations
```
- Consult the website Term of Use document (or website owner) before scraping data to find policy about request volume. Don't get your IP blocked!


### Python's Requests Library
- *standard library for making HTTP requests in Python: ```import requests```.*
  - ```$ pip install requests```
- **GET Request**: *trying to get or retrieve data from a source, in the form of a Response instance*
  - ```response = requests.get()``` => ```<Response [200]>```
- _**Status Code**_: ```response.status_code``` => ```200```
  - *200: Success, 204: No Content, 304: Not Modified, 404: Page Not Found*
    - ```if response: print("Success!")```: *```requests``` will evaluate True if the status code is between 200-400, otherwise False.*
    - ```try: response = requests.get(url)```: *try/except will raise an exception if request was unsuccessful.*
- _**Content**_: *Response of GET request contains information called a 'payload' in the message body. The response is actually serialized JSON content. Use ```response.json()``` to transform into a dictionary.*
  - ```response.content``` => *(...response's content in bytes...)*
  - ```response.text``` => *(...converted into a string, usually based on UTF-8 in the response's headers)* <- (```response.encoding = 'utf-8'```)
  - _**Headers**_: *Useful information, such as content type of response payload, time-limits on how long to cache the response, &c.*
    - ```response.headers```: *returns a dict-like object, header values are accessible by key, e.g. ```response.headers['content-type']``` => ```'application/json; charset=utf-8'```*
  - _**Query String Parameters**_: *customize a GET request by passing values in the URL*
    - ```response = requests.get('https://api.github.com/search/repositories', params={'q': 'requests+language:python'},)```
- TBD . . .


<hr>

### More BeautifulSoup Tools
- **```list(soup.children)```:** *since HTML tags are nested, we can move through the structure one level at a time. To select all the elements at the top level of the page, use the ```.children``` property of the ```soup``` object. Note: returns a list generator, so use ```list()``` on it.*
```python
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify) # ALL the HTML content
# # # 
print(list(soup.children)) #
print([type(item) for item in list(soup.children)])
```
```bash
<!DOCTYPE html>
<html>
 <head>
  <title>
   A simple example page
  </title>
 </head>

 <body>
  <p>
   Here is some simple content for this page.
  </p>
 </body>
</html>


['html', '\n', <html>
<head>
<title>A simple example page</title>
</head>
<body>
<p>Here is some simple content for this page.</p>
</body>
</html>]


[<class 'bs4.element.Doctype'>, <class 'bs4.element.NavigableString'>, <cla
ss 'bs4.element.Tag'>]
```






### Robots.txt
https://developers.google.com/search/docs/advanced/robots/intro?hl=en&visit_id=637408797717484153-3352655891&rd=1




<hr>

### SOURCES
- [A Practical Introduction to Web Scraping in Python](https://realpython.com/python-web-scraping-practical-introduction/): *this file is a summarized reproduction of this guide*
- [Beautiful Soup: Build a Web Scraper with Python](https://realpython.com/beautiful-soup-web-scraper-python/)
- [DataQuest Beautiful Soup tutorial](https://www.dataquest.io/blog/web-scraping-tutorial-python/)
