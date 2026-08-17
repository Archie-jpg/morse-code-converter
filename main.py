import sys
from typing import NoReturn

LETTERS_TO_MORSE_CODE = {"a": ". -", "b": "- . . .", 
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
                         "9": "- - - - .", "0": "- - - - -",
                         " ": "       "}

def print_options() -> NoReturn:
    """Output the options user may choose from"""
    print("1) Convert from plain text to morse code")
    print("2) Convert from morse code to plain text")
    print("3) Exit the program")
    
def convert_pt_to_mc(plain_text: str) -> str:
    """Takes in a string in plain text, checks that it can be converted, returning the resulting morse code if it can. If it cannot
    be converted, throws a value error.
    i.e "Hello world" is converted to 

    Args:
        plain_text (str): A string containing only the letters a-z, the numbers 1-9 and spaces in lower case
        
    Returns:
        str: Morse code version of input string
        
    Raises:
        ValuesError: If the string contains any invalid characters (i.e *). This first invalid character is contained within the 
        error message
    """
    output_string: str = ""
    for letter in plain_text:
        try: 
            output_string += LETTERS_TO_MORSE_CODE[letter]
            output_string += "   "
        except KeyError:
            raise ValueError(f"{letter} is not convertable to morse code.")
    return output_string


def main() -> NoReturn:
    print("Welcome to the morse code converter")
    print("To begin, please enter the number of an option below")
    print_options()
    option = "0"
    while option != "3":
        option = input("Option: ")
        if option == "1":
            plain_text = input("String to be converted: ").lower()
            morse_code = convert_pt_to_mc(plain_text=plain_text)
            print(f"Morse code: {morse_code}")
        elif option == "2":
            print("Option currently unavalible")
    return

    
if __name__ == "__main__":
    sys.exit(main())