def encrypt_this(text):
    cipher = ""
    for word in text.split():
        string = str(ord(word[0])) + (word[-1:] if len(word) > 2 else "") + word [2:-1] + word[1:2] + " "
        cipher += string
    return cipher[:-1]

"""
Encrypt this!
    You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:
Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter needs to be converted to its ASCII code.
The second letter needs to be switched with the last letter
Keepin' it simple: There are no special characters in input.
"""
