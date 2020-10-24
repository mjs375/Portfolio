def generate_markdowns(markdown, text, url_or_language): # all strings
    if markdown == "link":
        return f"[{text}]({url_or_language})"
    elif markdown == "img":
        return f"![{text}]({url_or_language})"
    else: # if markdown == "code":
        print(markdown, "|*|", text, "|*|", url_or_language)
        return f"```{url_or_language}\n{text}\n```"



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
    
