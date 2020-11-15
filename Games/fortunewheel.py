import csv
import random
import os # os.system('clear')
import re
import time


# Get all phrases from CSV file:
phrasebook = {}
with open('phrases.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for phrase, length in csv_reader:
        phrasebook[phrase] = length # create dict key/value pair
# Randomly select a phrase
phrase = random.sample(list(phrasebook), 1)[0]
unused = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # letters unused in each round
used = "" # already-guessed letters

#
#

def display():
    os.system('clear')
    show = " ".join(phrase) # add a space between all letters
    print("(",show,")")
    puzzle = re.sub(f"[{unused}]", "_", show) # hide every letter that hasn't been revealed
    print("Guessed letters:",unused)
    print(puzzle)


def wheel_spin():
    pass




display()


"""PSEUDOCODE:
[1. Open and save CSV file contents as dict
[2. Randomly select a phrase
[3. Create shadow-copy of string that shows a '_' for every letter, but keeps spaces and punctuation (dashes, apostrophes) as is.
4. Display 'board' and bank of letters already guessed.
  - How to play -
5. Spin wheel: if you guess a consonant and get it, you get the $amount the wheel landed on (multiplied by times letter appears in phrase).
    6. If correct: spin again, buy a vowel ($250), and attempt to 'solve'. Players can keep guessing vowels as long as they have the money and guess right.
6. Next player (if you incorrectly guess consonant or are done)
    - AI 'next player' randomly guesses a consonant. If they guess right, they randomly choose a subsequent action too. If they try to solve, they guess right/wrong based on % of word revealed.

"""
