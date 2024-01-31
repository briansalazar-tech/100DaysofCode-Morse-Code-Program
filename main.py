morse_code_dict = {
    "A" : ".- ",
    "B" : "-... ",
    "C" : "-.-. ",
    "D" : "-.. ",
    "E" : ". ",
    "F" : "..-. ",
    "G" : "--. ",
    "H" : ".... ",
    "I" : ".. ",
    "J" : ".--- ",
    "K" : "-.- ",
    "L" : ".-.. ",
    "M" : "-- ",
    "N" : "-. ",
    "O" : "--- ",
    "P" : ".--. ",
    "Q" : "--.- ",
    "R" : ".-. ",
    "S" : "... ",
    "T" : "- ",
    "U" : "..- ",
    "V" : "...- ",
    "W" : ".-- ",
    "X" : "-..- ",
    "Y" : "-.-- ",
    "Z" : "--.. ",
    "1" : ".---- ",
    "2" : "..--- ",
    "3" : "...-- ",
    "4" : "....- ",
    "5" : "..... ",
    "6" : "-.... ",
    "7" : "--... ",
    "8" : "---.. ",
    "9" : "----. ",
    "0" : "----- ",
    " " : "/ ",
    "." : ".-.-.- ",
    "!" : "-.-.-- ",
    "?" : "..--.. ",
}

morse_code_word = ""
deciphered_word = ""

while True:  
    operation = input("1 - Translate to Morse Code\n2 - Decipher Morse Code\n3 - Quit program\n\nPick a numerical option above: ")
    # Convert to morse code
    if operation == "1":
        morse_code_word = ""
        translate = input("\nPhrase or word to translate to morse code: ").upper()
        for letter in translate:
            if letter in morse_code_dict:
                morse_code_word += morse_code_dict[letter]
            else:
                letter += " "
                morse_code_word += letter 
        print(f"\nThe translated word is:\n{morse_code_word}\n\n")
    # Convert from morse code
    elif operation == "2":
        word_to_decipher = input("\n1 - Decipher current word\n2 - Decipher other translation\nPick an option above: ")
        # Convert existing word
        if word_to_decipher == "1":
            morse_letters = morse_code_word.split(" ")
            
            for i in range(len(morse_letters)):
                morse_letters[i] = morse_letters[i] + " "
            for letter in morse_letters:
                try:
                    translated_letter = list(morse_code_dict.keys())[list(morse_code_dict.values()).index(letter)]
                    deciphered_word += translated_letter
                except:
                    letter = letter.replace(" ", "")
                    deciphered_word += letter
            print(f"\nDeciphered word/phrase: {deciphered_word}\n\n")
            deciphered_word = ""
        # Convert new word
        elif word_to_decipher == "2":
            morse_code_word = input("\nEnter morse code to decipher: ")
            morse_letters = morse_code_word.split(" ")
            for i in range(len(morse_letters)):
                morse_letters[i] = morse_letters[i] + " "
            for letter in morse_letters:
                try:
                    translated_letter = list(morse_code_dict.keys())[list(morse_code_dict.values()).index(letter)]
                    deciphered_word += translated_letter
                except:
                    letter = letter.replace(" ", "")
                    deciphered_word += letter
            print(f"\nDeciphered word/phrase: {deciphered_word}\n\n")
            deciphered_word = ""
    # Exit
    elif operation == "3":
        print("Exiting...")
        break