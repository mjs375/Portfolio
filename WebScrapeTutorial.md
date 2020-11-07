## W E B _ S C R A P I N G

- Step 1: Obtain the HTML source-code in a string
```
from urllib.request import urlopen
  #
url = "http://website.com/you/wish/to/scrape"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)




```
