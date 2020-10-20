# hello example (words(more words) here) something

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
            
      
