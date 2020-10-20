# # # # # # # # # # # # C L E A N _ C O D E : # # # # # # # # # # # #

def remove_parentheses(s):
    ans, counter = "", 0 
        
    for letter in s:
        if letter == ")":
            counter += 1 # going 'out' of parentheses...
        elif letter == "(":
            counter -= 1 # when counter is -1 (-2, -3...), inside parentheses(s)
        elif counter == 0: #() are balanced 
            ans = ans + letter
            
    return ans


# # # # # # # # # # # # M E S S Y _ A T T E M P T _ N O . _ 1 : # # # # # # # # # # # #

def remove_parentheses(s):
    delete_switch = False
    ans = ""
    counter = 0 #assign counter '0' value. '0' = outside ALL ()s
        # will be -1, -2 if inside ()
        # will be 0 if outside () ['tab settled']
        
    for index, letter in enumerate(s):
        if letter == ")": #possibly exiting 'inside'
            counter = counter + 1
            if counter == 0: #() have 'balanced out', now outside
                delete_switch = False
            else:
                pass
        elif delete_switch == True: # inside (), don't add to 'ans'
            if letter =="(":
                counter = counter - 1
            continue
        elif letter == "(":
            counter = counter - 1
            delete_switch = True
        #
        else: #outside all (), add the letter to new string 'ans'
            ans = ans + s[index]
            
    return ans
            
      
"""
In this kata you are given a string for example:
    "example(unwanted thing)example"
Your task is to remove everything inside the parentheses as well as the parentheses themselves.
The example above would return:
    "exampleexample"
 Another example:
    "hello example (words(more words) here) something" >>> "hello example  something
"""
