## W E B _ S C R A P I N G _ I N _ P Y T H O N

- Gather the HTML source-code in a string:
```
from urllib.request import urlopen # Tools for working with URLs (urlopen() can open a URL within a program)
url = "http://website.com/you/wish/to/scrape" # website URL to be opened for scraping
page = urlopen(url) # opens the webpage, returns an 'HTTPResponse object (e.g. 'http.client.HTTPResponse object at 0x105fef820')
html_bytes = page.read() # .read() returns a sequence of bytes
html = html_bytes.decode("utf-8") # decodes bytes into a string, using UTF-8
print(html) # 'html' now contains all the HTML source code in a string
```
- Methods of Extracting Data between HTML tags:
  - String Methods:
    - ...
