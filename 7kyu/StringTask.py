def string_task(s):
    ans = ""
    # LOWERCASE
    s = s.lower()
    # DELETE VOWELS
    for l in s:
        if l in ["a", "e", "i", "o", "u", "y"]:
            s = s.replace(l,"") #replaces all instances of that 'l' with ""    
    # DOTS BEFORE CONSONANTS:
    for i in range(len(s)): #loop over length(of string)
        ans += "." + s[i]
    return ans

"""
Petya started to attend programming lessons. On the first lesson his task was to write a simple program. The program was supposed to do the following: in the given string, consisting of uppercase and lowercase Latin letters, it: 
 - deletes all the vowels, 
 - inserts a character "." before each consonant, 
 - replaces all uppercase consonants with corresponding lowercase ones.
Examples:
    ('tour')      =>  '.t.r'
    ('Codewars')  =>  '.c.d.w.r.s'
    ('aBAcAba')   =>  '.b.c.b'
"""
