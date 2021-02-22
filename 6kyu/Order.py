import re

def order(sentence):
    if sentence == [] \
    or all('' == s or s.isspace() for s in sentence):
        return ""
    
    #--Listify the words:
    words = sentence.split(" ")
    order = ["" for i in range(len(words))]
    print(order)
    #--
    for word in words:
        num = re.findall('[0-9]+',word)
        print(num[0], word)
        #--DON'T take out actual number, oops..
        #word = re.sub(num[0],"",word)
        #print(word)
        order[ int(num[0])-1 ] = word
    #--Assemble the order
    my_order = " ".join(order)
    print(my_order.strip())
    return my_order.strip()




"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
  Ex. "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"""
