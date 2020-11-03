def encode(n,msg):
    for i in range(n): # 5. Repeat steps 1-4 'n' times in total. 
    # 1. Remove all spaces (but remember positions)
        # a. Add string spaces indices to list:
        spaces = [] 
        for i, char in enumerate(msg):
            if char == " ":
                spaces.append(i)
        # b. Remove spaces
        msg = msg.replace(" ","")
    # 2. Shift order of chars to right by 'n' characters
        msg = msg[n:] + msg[:n]
    # 3. Put the spaces back in their original positions
        for i, char in enumerate(msg):
            if i in spaces:
                msg = msg[:i] + " " + msg[i:]
    # 4. Shift the characters of each substring (separated by spaces) to the right by 'n'
        # a. Break string into substrings separated by " "
        subs = msg.split()
        # b. Shift substring by 'n'
        for i,sub in enumerate(subs):
            m = n % len(sub)
            subs[i] = sub[m:] + sub[:m]
        msg = " ".join(subs)
# 6. Prepend "{n} " to the front of the encoded string.
    msg = f"{n} " + msg
    return msg













def decode(strng):
	#print(strng)
	pass
