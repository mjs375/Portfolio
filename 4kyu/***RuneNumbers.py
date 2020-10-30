import re
def solve_runes(runes):
    print(runes,type(runes))
    
    #string = "4+46=101/234*234-23"
    y = re.split('[+\-*/=]',runes)
    print(y) 
    
    #HANDLE NEGATIVE SIGNS: PUT BACK IN IF A SPACE IN THE LIST OF SPLITS
    
    pass
