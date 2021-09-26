"""
Write a regex expression to capture:
    0. the set of all alphabetic strings,
    1. the set of all lower-case alphabetic strings ending in `b`
    2. the set of all strings from the alphabet `a,b` such that each `a` is immediately preceded by and immediately followed by `b`
Write a regex expression to capture the following. By "word" we mean an alphabetic string separated from other words by whitespace, any relevant punctuation, line breaks, and so forth.
    3. the set of all strings with 2 consecutive repeated words (e.g. "Humbert Humbert" & "the the" but not "the bug" or "the big bug")
    4. All strings that start at the beginning of the line with an integer and that end at the end of the line with a word
    5. All strings that have both the word `grotto` and the word `raven` in them (but not words like `grottos` that merely contain the word `grotto`.)
        - I'm interpreting this question to mean you can *have* 'grottos' & 'ravens', but merely that those don't satisfy the condition to match; not that having those words disqualify the whole string as otherwise passing.
    6. Write a pattern that places the first word of an English sentence in a register. Deal with punctuation.
"""


import re
import string




def reginald():
    """
    Solve a series of regex problems:
    """
    patterns = [
        "^[a-zA-Z\s]*$", # ^[a-zA-Z]*$ : if whitespaces aren't allowed
        "^[a-z]*b$",
        "^(b+(ab+)*)$",
        r"^([a-zA-Z]*) \1$", # \1 is a back-reference so you match previous match, whatever it is
        "^[0-9]+.*[a-zA-z]+$",
        r"\braven\b.*\bgrotto\b|\bgrotto\b.*\braven\b",
        "(^(?i)[A-Z][a-z|[:punct:]]*\b)", # (^(?i)[A-Z][a-z|[:punct:]]*\b)(?:.*?)(?i)\b\1\b
    ]
    answers = [ [] for _ in patterns ] # list of lists for all answers to each Q
    Q = -1 # which question we're on

    #--Open the file
    with open("regex_practice.txt") as file:

        #--Run line by line:
        for line in file:

            #--Skip line of notes:
            if line[0] == "#":
                Q += 1
                continue

            #--Remove trailing/starting whitespace (`\n`)
            line = line.strip()

            if patterns[Q]:
                match = re.findall(patterns[Q], line)
                #print(match)
                if match:
                    #print(line)
                    answers[Q].append(line)
    #
    #
    return answers


#
#
answers = reginald()
for i, set in enumerate(answers):
    print(i, set)
# # # # # # #
