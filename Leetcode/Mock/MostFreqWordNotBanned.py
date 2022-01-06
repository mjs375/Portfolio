class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        
        for i in range( len(paragraph) ):
            if not paragraph[i].isalpha():
                paragraph = paragraph[:i] + " " + paragraph[i+1:]
        
        freq = {}
        
        for word in paragraph.lower().split():
            print(word)
            if word not in banned:
                if word not in freq:
                    freq[word] = 1
                else:
                    freq[word] += 1
        
        most,maxx = "",0
        for word, freq in freq.items():
            if freq > maxx:
                maxx = freq
                most = word
        return most
            
"""
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.

  Example 1:
    Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
    Output: "ball"
      Explanation: 
        - "hit" occurs 3 times, but it is a banned word.
        - "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
      Note that words in the paragraph are not case sensitive,
      that punctuation is ignored (even if adjacent to words, such as "ball,"), 
      and that "hit" isn't the answer even though it occurs more because it is banned.
      
  Example 2:
    Input: paragraph = "a.", banned = []
    Output: "a"
"""
