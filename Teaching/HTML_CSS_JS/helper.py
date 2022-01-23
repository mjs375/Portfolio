"""
Data processing file in Python for
HTML, CSS, JavaScript program "Wordly".

Produces a javascript file with a dictionary
of all five-letter words taken from larger
dictionary. Formats as a single JS array.
"""



with open('dictionary', 'r') as file:
    all = file.readlines()

# print(all[:10])

dictionary = []

for word in all:
    # strip `\n` character:
    word = word.strip()
    if len(word) == 5:
        dictionary.append(word.upper())

print(dictionary[:20])


with open('wordle_dictionary.js', 'w') as file:
    file.write("let dictionary = [ \n")

    for word in dictionary:
        line = "\"" + word + "\",\n"
        file.write(line)

    file.write("]")
print("Done!")
