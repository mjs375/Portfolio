"""

[a-zA-Z]+
    # any amount of letters, caps or not
[A-Z][a-z]*
    #
p[aeiou]{,2}t
    # p followed by any vowel up to x2 then a t, e.g. pout, pot, not poot
\d+(\.\d+)?
    # IDs a decimal, like 12.222 (multiple groups/matches: 12, .222, and 12.222)
([^aeiou][aeiou][^aeiou])*
    # finds any sub-match of 3 chars thats: not a vowel(consonant or digit or punc), a vowel, then not a vowel again. Doesn't allow double-use of chars, like in !ababababab => [!ab]a[bab]a[bab]a...
\w+|[^\w\s]+
    # \w => equivalent to [a-zA-Z0-9_]
    # finds any word character, or any non-word char or space, any amount of times


"""


from nltk import re_show # re_show(pattern, string)

p1 = "[a-zA-Z]+" # any alphabetical chunk, any length
s1 = "abcdefg123"
print( re_show(p1, s1) )

p2 = "[A-Z][a-z]*"
s2 = "Cassady"
# ...
#
