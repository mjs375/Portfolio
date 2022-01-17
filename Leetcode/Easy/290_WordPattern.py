class Solution:
    def wordPattern(self, pattern: str, sentence: str) -> bool:
        sentence = sentence.split()
        
        if len(pattern) != len(sentence):
            return False
        
        x = {}
        used  = []
        
        for word, letter in zip(sentence, pattern):
            print(word, letter)
            if letter in x.keys():
                if x[letter] != word:
                    print(x[letter], word)
                    return False
            else:
                if word not in used:
                    x[letter] = word
                    used.append(word)
                else:
                    return False
                
        return True
      
      

"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""
