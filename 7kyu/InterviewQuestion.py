def get_strings(city): # city = Chicago
    city = city.replace(" ", "")
    city = city.lower()
    solution = "" #empty string 
    star = "*"
    
    for i in range(len(city)):
        num = city.count(city[i]) #count instances of i-th letter
        temp = city[i] + ":" + star*num + ","
        if temp not in solution:
            solution = solution + temp
        
    return solution.rstrip(",") #strip the last "," from the string



"""
You receive the name of a city as a string, and you need to return a string that shows how many times each letter shows up in the string by using an asterisk (*).
    For example:
        "Chicago"  -->  "c:**,h:*,i:*,a:*,g:*,o:*"
As you can see, the letter c is shown only once, but with 2 asterisks.
The return string should include only the letters (not the dashes, spaces, apostrophes, etc). There should be no spaces in the output, and the different letters are separated by a comma (,) as seen in the example above.
Note that the return string must list the letters in order of their first appearence in the original string.
    More examples:
        "Bangkok"    -->  "b:*,a:*,n:*,g:*,k:**,o:*"
        "Las Vegas"  -->  "l:*,a:**,s:**,v:*,e:*,g:*"
"""
