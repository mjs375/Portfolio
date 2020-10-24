def generate_markdowns(markdown, text, url_or_language): # all strings
    if markdown == "link":
        return f"[{text}]({url_or_language})"
    elif markdown == "img":
        return f"![{text}]({url_or_language})"
    else: # if markdown == "code":
        print(markdown, "|*|", text, "|*|", url_or_language)
        return f"```{url_or_language}\n{text}\n```"

    
# # # # # B E T T E R : # # # # # #
pattern = {
    'link': '[{txt}]({url_or_language})',
    'img':  '![{txt}]({url_or_language})',
    'code': "```{url_or_language}\n{txt}\n```",
} 
# dict of models:
    # key is markdown-type (link, img, code)
    # value is format of return

def generate_markdowns(markdown, txt, url_or_language):
    return pattern[markdown].format(txt=txt, url_or_language=url_or_language)
    # above asks for the dict key
        # formatted a
        
        
""" 
# Getting a Dict Value, where its value is a format string (feed it variables to insert to pattern)
    numberFormat = 'Count in Spanish: {one}, {two}, {three}, ...'
    withSubstitutions = numberFormat.format(one='uno', two='dos', three='tres')
    print(withSubstitutions)
# .format()
    txt = "For only {price:.2f} dollars!"
    print(txt.format(price = 49))
"""








"""
Your friend has recently started using Codewars to learn more advanced coding. They have just created their first kata, and they want to write a proper description for it, using codeblocks, images and hyperlinks. However, they are struggling to understand how to use Markdown formatting properly, so they decide to ask for your help, by having you write a program that will generate some of the syntaxes for you.
  Markdown syntaxes
    links: [displayed text](url address)
    images: ![replacement message](url address)
    codeblocks: we'll use multiline codeblocks like the following
```language
code
```
Task:
  Your task is to create a function called generate_markdowns or generateMarkdowns. It will take three parameters:
    markdown - The type of markdown to return. It can be "link", "img" or "code".
    text - The text,message or code to display
    url_or_language or urlOrLanguage - gives either the url address to use or the name of the language for the codeblock.
Examples
  generate_markdowns('link','Github Codewars','https://github.com/codewars')
    # returns: "[Github Codewars](https://github.com/codewars)"
"""








""" ATTEMPT TO TERNARY EXPRESS:
    return markdown == "link" and f"[{text}]({url_or_language})"  #this works
    # <condition> and <what_to_evaluate_if_condition_True>
    # if <condition>: myList.append('myString')
    
    #return markdown == "img" and f"![{text}]({url_or_language})" #doesn't work
    if markdown == "img": f"![{text}]({url_or_language})"         #doesn't work

    return markdown == "code" and f"```{url_or_language}\n{text}\n```" #...
"""
    
