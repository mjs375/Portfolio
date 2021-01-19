def parse(data):
    output = []
    v = 0
    for c in data:
        if c == "i":
            v += 1
        elif c == "d":
            v -= 1
        elif c == "s":
            v *= v
        elif c == "o":
            output.append(v)
    return output
    
"""
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

parse("iiisdoso")  ==>  [8, 64]
"""
