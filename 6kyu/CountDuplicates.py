def duplicate_count(text):
    #count = {char: 0 for char in text}
    if text == "": return 0
    #--lowercase
    text = text.lower()
    count = {} # initialize
    for char in text:
        #--Check if char is a key yet:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    # check if any duplicates
    tally = 0
    for k,v in count.items():
        if v >= 2: tally += 1
    return tally

"""
Count the number of Duplicates
  Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
Example
  "abcde" -> 0 # no characters repeats more than once
  "aabbcde" -> 2 # 'a' and 'b'
  "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
  "indivisibility" -> 1 # 'i' occurs six times
  "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"""
