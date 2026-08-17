LETTERS_TO_MORSE_CODE: dict = {"a": ". -", "b": "- . . .", 
                         "c": "- . - .", "d": "- . .",
                         "e": ".", "f": ". . - .",
                         "g": "- - .", "h": ". . . .",
                         "i": ". .", "j": ". - - -",
                         "k": "- . -", "l": ". - . .",
                         "m": "- -", "n": "- .",
                         "o": "- - -", "p": ". - - .",
                         "q": "- - . -", "r": ". - .",
                         "s": ". . .", "t": "-",
                         "u": ". . -", "v": ". . . -",
                         "w": ". - -", "x": "- . . -",
                         "y": "- . - -", "z": "- - . .",
                         "1": ". - - - -", "2": ". . - - -",
                         "3": ". . . - -", "4": ". . . . -",
                         "5": ". . . . .", "6": "- . . . .",
                         "7": "- - . . .", "8": "- - - . .",
                         "9": "- - - - .", "0": "- - - - -"}
MORSE_CODE_TO_LETTERS: dict = {morse_code: letter for letter, morse_code in LETTERS_TO_MORSE_CODE.items()}

def pt_to_mc(plain_text: str) -> str:
    """Takes in a string in plain text, checks that it can be converted, returning the resulting morse code if it can. If it cannot
    be converted, raises a value error.
    i.e "Hello world" is converted to ". . . .   .   . - . .   . - . .   - - -          . - -   - - -   . - .   . - . .   - . ."

    Args:
        plain_text (str): A string containing only the letters a-z, the numbers 0-9 and spaces in lower case
        
    Returns:
        str: Morse code version of input string
        
    Raises:
        ValueError: If the string contains any invalid characters (i.e *). This first invalid character is contained within the 
        error message
    """
    output_string: str = ""
    for letter in plain_text:
        if letter == " ":
            output_string += " " * 7 # Add 7 spaces between words
        else:
            try: 
                output_string += LETTERS_TO_MORSE_CODE[letter]
                output_string += " " * 3 # Add three spaces between letters
            except KeyError:
                raise ValueError(f""""{letter}" is not convertable to morse code. Characters must be letters in a-z, numbers in 0-9 or spaces.""")
    return output_string

def mc_to_pt(morse_code: str) -> str:
    """Converts morse code to plain text. Raises an error if it is not valid morse code
    i.e ". . . .   .   . - . .   . - . .   - - -          . - -   - - -   . - .   . - . .   - . ." is converted to "Hello world"

    Args:
        morse_code (str): A string in morse code

    Returns:
        str: The plain text the morse code represents
        
    Raises:
        ValueError: If the string contains a morse code pattern that is not recognised. Error message contains unrecognised morse code string
    """
    output_string: str = ""
    for word in morse_code.split(" " * 10): # Split morse code into words
        print(word)
        for letter in word.split(" " * 3): # Split word into individual letters
            print(letter)
            try: 
                output_string += MORSE_CODE_TO_LETTERS[letter]
            except KeyError:
                raise ValueError(f""""{letter}" is not a recognised morse code pattern.""")
        output_string += " "
    return output_string
                