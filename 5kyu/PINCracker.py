import hashlib
#
def crack(hash):
    for i in range(0,100000): #iterate all possible PINs to brute-force crack
        PIN = str(i).zfill(5) #00000 >> 99999
        result = hashlib.md5(PIN.encode()) #step 1
        result = str(result.hexdigest()) #step 2
        if result == hash:
            return PIN 


"""
MD5 HASH IN PYTHON:
  - encode(): converts the string into bytes to be acceptable by hash function
  - digest(): returns the encoded data in *byte format*
  - hexdigest(): returns the encoded data in *hexadecimal format*
  
HASHING A PIN:
    pin2hash = '12345' #12345
    result = hashlib.md5(pin2hash.encode())
    result = str(result.hexdigest())
    return result #827ccb0eea8a706c4c34a16891f84e7b
    
    
    
Given is a md5 hash of a five digits long PIN. It is given as string. Md5 is a function to hash your password: "password123" ===> "482c811da5d5b4bc6d497ffa98491e38"
  Why is this useful? Hash functions like md5 can create a hash from string in a short time and it is impossible to find out the password, if you only got the hash. The only way is cracking it, means try every combination, hash it and compare it with the hash you want to crack. (There are also other ways of attacking md5 but that's another story) Every Website and OS is storing their passwords as hashes, so if a hacker gets access to the database, he can do nothing, as long the password is safe enough.
  Your task is to return the cracked PIN as string.
This is a little fun kata, to show you, how weak PINs are and how important a bruteforce protection is, if you create your own login.
"""
