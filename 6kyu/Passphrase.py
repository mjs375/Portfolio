def play_pass(pwd, n):
    new, new2 = "", ""
    nums1 = "0123456789"
    nums2 = "9876543210"
    
    #--Shift chars, replace digits:
    for p in pwd:
        if p in nums1:
            comp = nums1.index(p) 
            new += nums2[comp]
        
        elif p.isalpha():
            if p.islower():
                temp = chr((ord(p)-97 +n)%26 + 97)
            elif p.isupper():
                temp = chr((ord(p)-65+n)%26 + 65)
            new += temp
        else:
            new += p
    #--Downcase odds, uppercase evens
    for i, char in enumerate(new):
        if char.isalpha():
            if i % 2 == 0: #even
                char = char.upper()
            else: # odd
                char = char.lower()
        new2 += char
    #--Reverse entire string
    return new2[::-1]
        



"""
Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they can be guessed due to common cultural references. You can get your passphrases stronger by different means. One is the following:
  - choose a text in capital letters including or not digits and non alphabetic characters,
  - shift each letter by a given number but the transformed letter must be a letter (circular shift),
  - replace each digit by its complement to 9,
  - keep such as non alphabetic and non digit characters,
  -downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
  - reverse the whole result.
Example:
  your text: "BORN IN 2015!", shift 1
1 + 2 + 3 -> "CPSO JO 7984!"
4 "CpSo jO 7984!"
5 "!4897 Oj oSpC"
"""
