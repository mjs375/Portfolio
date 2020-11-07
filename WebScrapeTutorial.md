## W E B _ S C R A P I N G _ I N _ P Y T H O N

[Source](https://realpython.com/python-web-scraping-practical-introduction/)

### Gather the HTML source-code in a string:
```
from urllib.request import urlopen # Tools for working with URLs (urlopen() can open a URL within a program)

url = "http://website.com/you/wish/to/scrape" # website URL to be opened for scraping

page = urlopen(url) # opens the webpage, returns an 'HTTPResponse object (e.g. 'http.client.HTTPResponse object at 0x105fef820')

html_bytes = page.read() # .read() returns a sequence of bytes

html = html_bytes.decode("utf-8") # decodes bytes into a string, using UTF-8

print(html) # 'html' now contains all the HTML source code in a string
```


### Simple Method of Extraction:
- **String Methods**: *using .find() and string slicing syntax, you can pull the index range of HTML between 2 tags, e.g. <title>...</title>. This is a very simple method vulnerable to many failings: it can only find the first instance, if '<title>' is actually '<title id="hdg">' it won't find it, &c.*
  - ```.find()```: *searches a string for the first instance of the string-pattern*
```
# <title>Poseidon</title>
title_index = html.find("<title>") # get the index of the '<' in '<title>'
start_index = title_index + len("<title>") # get the index of the first letter of the actual title, "'P'oseidon"
end_index = html.find("</title>") # repeat for close tag
title = html[start_index:end_index]
print(title) # "Poseidon"
```
   

### Regular Expressions – Extracting Data between HTML tags:


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

### Creating and Saving a .CSV File with data









