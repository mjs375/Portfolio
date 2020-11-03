import re
#
def encode(n,msg):
    print("0:",msg) #TODO
    print()
    #
    if "\n" in msg: #handle the 2-character '\n' situation simply:
        msg = msg.replace("\n","|") #replace w/ uncommon character; replace again at end
        
    #
    original = msg #clean copy (for length purposes, &c.)

    
    for i in range(n): # 5. Repeat steps 1-4 'n' times in total. 
    # 1. Remove all spaces (but remember positions)
        # a. Add string spaces indices to list:
        spaces = [] 
        for i, char in enumerate(msg):
            if char == " ":
                spaces.append(i)
        # b. Remove spaces
        msg = msg.replace(" ","")
#        print("1:",msg) #TODO

        
    # 2. Shift order of chars to right by 'n' characters
        #msg = msg[n:] + msg[:n] #TODO: potential bug
        if n > len(msg):
            m = n % len(msg)
        else: m = n
        l = len(msg) - n
        if m == 0:
            msg = msg[-m:] #+ msg[:l]
        else:
            msg = msg[-m:] + msg[:l]
#        print("2:",msg) #TODO
        

    # 3. Put the spaces back in their original positions
        for i, char in enumerate(original): #
            if i in spaces:
                msg = msg[:i] + " " + msg[i:]
#        print("3:",msg) #TODO
        # 'eu niv erse .I fyou wi shtom ake anap plepiefr oms crat ch,yo umustf irs tinventth'

        

    # 4. Shift the characters of each substring (separated by spaces) to the right by 'n'
        # a. Break string into substrings separated by " "
        subs = msg.split()
        # b. Shift substring by 'n'
        for i,sub in enumerate(subs):
            if n > len(sub):
                m = n % len(sub) # 0 = 10 % 2 
            else: m = n
            l = len(sub) - m # 2 = 2 - 0
            if m == 0: #prevent duplication of substring:
                subs[i] = sub[-m:]
            else:
                subs[i] = sub[-m:] + sub[:l] # sub[0:] + sub[2:]
        msg = " ".join(subs)
#        print("4:",msg) #TODO
        # 'eu vni seer .I oufy wi shtom eak apan frplepie som atcr ch,yo ustfum sir htinventt'

    # (Exit n-times loop, final step:)
# 6. Prepend "{n} " to the front of the encoded string.
    if "|" in msg:
        msg = msg.replace("|","\n")
    msg = f"{n} " + msg
    return msg








def decode(cipher):
    print("0:",cipher) #TODO
    print()
    # 0a. Identify 'n':
    x = re.match("[0-9].", cipher)
    n = int(x[0])
    # 0b. Delete "n " from start of string
    j = cipher.find(" ")
    j = j + 1
    cipher = cipher[j:]
    # 0c. handle the 2-character '\n' situation simply:
    if "\n" in cipher:
        cipher = cipher.replace("\n","*") #replace w/ uncommon character; replace again at end   
    print(n,cipher)
    #
    original = cipher #clean copy (for length purposes, &c.)
    #
    #
    #
    for i in range(n): # 5. Repeat steps 1-4 'n' times in total. 
    # 1. Remove all spaces (but remember positions)
        # a. Add string spaces indices to list:
        spaces = [] 
        for i, char in enumerate(cipher):
            if char == " ":
                spaces.append(i)
        # b. Remove spaces
        cipher = cipher.replace(" ","")
#        print("1:",cipher) #TODO

        
    # 2. Shift order of chars to right by 'n' characters
        if n > len(cipher):
            m = n % len(cipher)
        else: m = n
        l = len(cipher) - n
        if m == 0:
            cipher = cipher[-m:] #+ msg[:l] #TODO??!?!?!?!?!?!
        else:
            cipher = cipher[:l] + cipher[-m:]
#        print("2:",cipher) #TODO
        

    # 3. Put the spaces back in their original positions
        for i, char in enumerate(original): #
            if i in spaces:
                cipher = cipher[:i] + " " + cipher[i:]
#        print("3:",cipher) #TODO
        # 'eu niv erse .I fyou wi shtom ake anap plepiefr oms crat ch,yo umustf irs tinventth'

        

    # 4. Shift the characters of each substring (separated by spaces) to the right by 'n'
        # a. Break string into substrings separated by " "
        subs = cipher.split()
        # b. Shift substring by 'n'
        for i,sub in enumerate(subs):
            if n > len(sub):
                m = n % len(sub) # 0 = 10 % 2 
            else: m = n
            l = len(sub) - m # 2 = 2 - 0
            #
            if m == 0: #prevent duplication of substring:
                subs[i] = sub[-m:]
            else:
                subs[i] = sub[:l] + sub[-m:] # sub[0:] + sub[2:]
        cipher = " ".join(subs)
#        print("4:",msg) #TODO
        # 'eu vni seer .I oufy wi shtom eak apan frplepie som atcr ch,yo ustfum sir htinventt'

    # (Exit n-times loop, final step:)
# 6. Prepend "{n} " to the front of the encoded string.
    if "*" in cipher:
        cipher = cipher.replace("*","\n")
    cipher = f"{n} " + cipher
    return cipher
