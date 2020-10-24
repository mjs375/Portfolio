class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = str(map1) #plaintext
        self.map2 = str(map2) #code
        pass
    
    def encode(self, s):
        code = ""
        for letter in s: #iterate the message
            if letter.isalpha():
                for i in range(26):
                    if letter in self.map1[i]: #find index of letter in plaintext
                        code = code + self.map2[i]
                        break #stop the inner loop, already found index-match
            else: #special characters...
                code = code + letter        
        return code
    
    def decode(self, s):
        plaintext = ""
        for letter in s: #iterate the message
            if letter.isalpha(): # if a-z:
                for i in range(26): #iterate len(alphabet)
                    if letter in self.map2[i]: #find index of letter in plaintext
                        plaintext = plaintext + self.map1[i]
                        break #stop the inner loop, already found index-match
            else: #special characters...
                plaintext = plaintext + letter        
        return plaintext





"""
A simple substitution cipher replaces one character from an alphabet with a character from an alternate alphabet, where each character's position in an alphabet is mapped to the alternate alphabet for encoding or decoding.
  E.g.
map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";

cipher = Cipher(map1, map2);
cipher.encode("abc") # => "eta"
cipher.encode("xyz") # => "qxz"
cipher.encode("aeiou") # => "eirfg"

cipher.decode("eta") # => "abc"
cipher.decode("qxz") # => "xyz"
cipher.decode("eirfg") # => "aeiou"
"""

















# # # # # # # # # # # # # # # #
# This fails b/c of my assumption that map1 will always be abc...xyz. FALSE!
# # # # # # # # # # # # # # # # 


"""
ord(a)     => 65 # gives ASCII number from letter
char(65)   => a  # gives letter from ASCII position
"""
class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = str(map1) # refname: self.map1
        self.map2 = str(map2) # refname: self.map2
        pass
    
    
    def encode(self, s):
        print("Encode:",s)
        encoded = ""  
        for letter in s:
            i = 0 # reset index   #A:65, a:97 (ASCII)
            if letter.isalpha():
                i = ord(letter) - 97
                encoded = encoded + self.map2[i]
            else: #keep letter as is
                encoded = encoded + letter # get scrambled letter and add to encoded-string
        print("Encoded:",encoded)
        return encoded
    
    
    def decode(self, s):
        print("Decode:",s)
        decoded = ""
        for letter in s:
            j = 0 
            #if letter in "abcdefghijklmnopqrstuvwxyz":
            j = ord(letter) - 97 # all lowercase.
            try:
                decoded = decoded + self.map1[j]
            except:
                decoded = decoded + letter
        print("Decoded:",decoded)
        return decoded
    
    
    
    
"""
if letter.isupper():
    j = ord(letter) - 65
if letter.islower():
    j = ord(letter) - 97
"""
    
