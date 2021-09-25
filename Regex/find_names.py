import re
import string

# Usage: `$ python regex.py > g.txt`

""" Program aims:
Catch any of the extremely various spellings of Momar Gaddafi's name,
while still excluding near or too-mispelled versions.

Use the following site to develop the regex pattern easily:
    https://regex101.com/
"""
pattern = "[gkq](?:a|u|ua|ha|he)(?:dhdh|dh|d{1,2}|th|dth|ddh|[z]+)[a]f{1,2}[iy][^y]" # regex pattern
#--If you don't remove the punctuation (`'`)
#pattern = "[gkq](?:a|u|ua|ha|he)(?:dhdh|dh|d{1,2}|th|dth|ddh|[z]+)'[a]f{1,2}[iy][^y]" # regex pattern


output = [] # matching names


def find_names():
    #--Open the file
    with open("gaddafi.txt") as file:

        #--Run line by line:
        for i, line in enumerate(file):

            #--Skip line of notes:
            if line[i] == "#":
                continue

            #--Date cleanup:
            line = line.lower() # lowercase
            line = line.translate(None, string.punctuation)

            #--Apply regex to find matches:
            match = re.findall(pattern, line)
            #print(match)
            if match:
                print(line)
                output.append(line)

    #print(output)
    print( len(output) )

#
#
#
find_names()
# # # # # # #
