def DNA_strand(dna):
    DNA = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
    }
    strand = ""
    for n in dna:
        strand += DNA[n]
    return strand
    
"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
  Example: (input: output)
    DNA_strand ("ATTGC") # return "TAACG"
    DNA_strand ("GTAT") # return "CATA"
"""
