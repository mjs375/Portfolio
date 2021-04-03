def tap_code_translation(text):
    #--Code:
    alphabet = 'abcdefghijlmnopqrstuvwxyz'
    
    text = text.replace('k','c')
    text = text.lower()
    
    msg = ""
    
    for char in text:
        tip = (alphabet.index(char) // 5) + 1
        tap = (alphabet.index(char) % 5) + 1
        msg += tip*"." + " " + tap*"." + " "
    return msg.strip()
  
"""
  Tap code is a way to communicate using a series of taps and pauses for each letter. In this kata, we will use dots . for the taps and whitespaces for the pauses.

The number of taps needed for each letter matches its coordinates in the following polybius square (note the c/k position). Then you "tap" the row, a pause, then the column. Each letter is separated from others with a pause too.

   1  2  3  4  5
1  A  B C\K D  E
2  F  G  H  I  J
3  L  M  N  O  P
4  Q  R  S  T  U
5  V  W  X  Y  Z
Input:
A lowercase string of a single word (no whitespaces or punctuation, only letters).

Output:
The encoded string as taps and pauses.

Examples
text = "dot"
  "D" = (1, 4) = ". ...."
  "O" = (3, 4) = "... ...."
  "T" = (4, 4) = ".... ...."
  
output: ". .... ... .... .... ...."
"""
