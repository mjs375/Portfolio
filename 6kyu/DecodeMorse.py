def decodeMorse(morse_code):
    words = morse_code.split(" ")
    plaintext = ""
    for i, word in enumerate(words):
        if word == "":
            plaintext += " "
        else:
            for k, v in MORSE_CODE.items(): #included dictionary to translate morse/letters
                if word == k:    
                    plaintext += v
    return " ".join(plaintext.split())
