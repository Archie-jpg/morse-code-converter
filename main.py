import sys
from typing import NoReturn

import converter

def print_options() -> NoReturn:
    """Output the options user may choose from"""
    print("To continue, please enter the number of an option below")
    print("1) Convert from plain text to morse code")
    print("2) Convert from morse code to plain text")
    print("3) Exit the program")
    

def convert_to_morse_code() -> NoReturn:
    """Takes in a plain text string from the user outputs the morse code equivalent"""
    plain_text = input("String to be converted: ").lower()
    while plain_text != "":
        try:
            morse_code = converter.pt_to_mc(plain_text=plain_text)
            print(f"Morse code: {morse_code}")
            input()
            print("Enter another string to convert again, or press enter to return to menu")
        except ValueError as e:
            print(e)
            print("Please renter string to try again, or press enter to return to menu")
        plain_text = input("String to be converted: ").lower()
        print(plain_text)


def main() -> NoReturn:
    print("Welcome to the morse code converter")
    option = "0"
    while option != "3":
        print_options()
        option = input("Option: ")
        if option == "1":
            convert_to_morse_code()
        elif option == "2":
            input("Option currently unavalible")
    return

    
if __name__ == "__main__":
    sys.exit(main())