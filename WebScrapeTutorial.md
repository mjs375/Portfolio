## W E B _ S C R A P I N G _ I N _ P Y T H O N

### Gather the HTML source-code in a string:
```
from urllib.request import urlopen 
  # Tools for working with URLs (urlopen() can open a URL within a program)
url = "http://website.com/you/wish/to/scrape" 
  # website URL to be opened for scraping
page = urlopen(url) 
  # opens the webpage, returns an 'HTTPResponse object (e.g. 'http.client.HTTPResponse object at 0x105fef820')
html_bytes = page.read() 
  # .read() returns a sequence of bytes
html = html_bytes.decode("utf-8") 
  # decodes bytes into a string, using UTF-8
print(html) 
  # 'html' now contains all the HTML source code in a string
```
### Methods of Extracting Data between HTML tags:
- **String Methods**: *using .find() and string slicing syntax, you can pull the index range of HTML between 2 tags, e.g. <title>...</title>*
  - ```.find()```: *searches a string for the first instance of the string-pattern*
```
# <title>Poseidon</title>
title_index = html.find("<title>") # get the index of the '<' in '<title>'
start_index = title_index + len("<title>") # get the index of the first letter of the actual title, "'P'oseidon"
end_index = html.find("</title>") # repeat for close tag
title = html[start_index:end_index]
print(title) # "Poseidon"

```
   
