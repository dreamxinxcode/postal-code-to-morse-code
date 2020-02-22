# Dictionary of letters and numbers.
CHARS = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
         'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', }


def ascii_to_morse(chars):
    morse = ""
    chars = chars.upper()  
    for char in chars:
        if(char in CHARS):
            morse += CHARS[char] + " "  # Appends key to 'morse' string.
        if(char == " "):
                morse += " "
        elif(char not in CHARS):
            raise Exception("Error! Enter a valid postal code")
    return morse


def main():
    postal_code = input("Enter a postal code: ")
    print(ascii_to_morse(postal_code))


if __name__ == "__main__":
    main()
