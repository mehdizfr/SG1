"""
Programming Language:
    Python 3

Development Environment:
    Thonny IDE

Course:
    CMP SCI 4500 - Software Development
    Fall 2026

Group:
    Group _____

Programmers:
    Mehdi Zafferi
    Rahul Anilkumar
    Klara Pere
    Scott Smith
    Armando Montoya

Original Development Date:
    October 4, 2026

Major Revision Dates:
    October 7, 2026 - Improved filename validation and documentation.

Program Description:
    SG1 is an interactive Python 3 program that reads a text file
    containing rows of binary digits. The program validates the text
    file, displays its contents, and converts the binary data into a
    black-and-white PNG image named IMAGE1.PNG.

    The program also reads IMAGE2.PNG, which is a 250 by 250
    black-and-white image. The pixels from IMAGE2.PNG are converted
    into a two-dimensional structure containing zeros and ones.

    SG1 searches this structure for a specified 11 by 11 plus-sign
    pattern. The program reports how many copies of the pattern are
    found and the coordinates of the center of each detected pattern.

    Finally, SG1 creates IMAGE3.PNG based on IMAGE2.PNG. White
    background pixels belonging to detected patterns are changed
    to red while the black pixels remain black.

Central Data Structures:
    The program uses a list of strings named lines to store the rows
    read from the binary text file.

    The program will also use a two-dimensional list named
    ZerosAndOnes to represent pixels from IMAGE2.PNG. Black pixels
    are represented by 0 and other pixel values are represented by 1.

External Files:
    User-selected .txt file:
        Contains rows of binary digits used to create IMAGE1.PNG.

    IMAGE1.PNG:
        Generated from the binary text file.

    IMAGE2.PNG:
        A 250 by 250 black-and-white input image used for pattern
        detection.

    IMAGE3.PNG:
        Generated from IMAGE2.PNG after detected pattern backgrounds
        are changed to red.

External Resources:
    ChatGPT:
        Used for assistance with the GetTextFileName function.

    Any additional resources used during development should be added
    here before submission.
"""


def GetTextFileName():
    """
    Purpose:
        Prompts the user for a valid Windows 11 text filename and
        continues prompting until a valid filename ending in .txt
        is entered.

    Global Variables:
        None.

    Parameters:
        None.

    Returns:
        A string containing a valid filename ending in .txt.
    """

    # GetTextFileName was developed with assistance from ChatGPT.

    invalid_characters = '<>:"/\\|?*'

    reserved_names = {
        "CON", "PRN", "AUX", "NUL",
        "COM1", "COM2", "COM3", "COM4", "COM5",
        "COM6", "COM7", "COM8", "COM9",
        "LPT1", "LPT2", "LPT3", "LPT4", "LPT5",
        "LPT6", "LPT7", "LPT8", "LPT9"
    }

    while True:
        filename = input(
            "Enter the name of the text file, including .txt: "
        )

        if filename == "":
            print("Error: filename cannot be empty.")
            continue

        if filename.strip() == "":
            print("Error: filename cannot contain only spaces.")
            continue

        if filename != filename.strip():
            print("Error: filename cannot begin or end with a space.")
            continue

        if not filename.lower().endswith(".txt"):
            print("Error: filename must end with .txt.")
            continue

        invalid_found = False

        for character in invalid_characters:
            if character in filename:
                print(
                    "Error: filename contains the invalid character "
                    + character
                )
                invalid_found = True
                break

        if invalid_found:
            continue

        base_name = filename.rsplit(".", 1)[0]

        if base_name.upper() in reserved_names:
            print(
                "Error: " + base_name
                + " is a reserved Windows filename."
            )
            continue

        if len(filename) > 255:
            print("Error: filename is too long.")
            continue

        return filename


# ------------------------------------------------------------
# Program introduction
# ------------------------------------------------------------

print("SG1 Program")
print("This program reads a binary text file and works with images.")


# ------------------------------------------------------------
# Get the name of the text file.
# ------------------------------------------------------------

filename = GetTextFileName()


# ------------------------------------------------------------
# Open and validate the binary text file.
# ------------------------------------------------------------

try:
    file = open(filename, "r")
    data = file.read()
    file.close()

    lines = data.splitlines()

    # Make sure the file contains only binary characters.
    for line in lines:
        if any(char not in "01" for char in line):
            print("Error: file must contain only 0s and 1s.")
            input("Press ENTER to end.")
            raise SystemExit

    # The file must contain at least 10 lines.
    if len(lines) < 10:
        print("Error: file must have at least 10 lines.")
        input("Press ENTER to end.")
        raise SystemExit

    length = len(lines[0])

    # Each line must contain at least 20 characters.
    if length < 20:
        print("Error: each line must have at least 20 characters.")
        input("Press ENTER to end.")
        raise SystemExit

    # All lines must contain the same number of characters.
    for line in lines:
        if len(line) != length:
            print("Error: all lines must have the same length.")
            input("Press ENTER to end.")
            raise SystemExit

    # Display the contents of the valid text file.
    print(data)

except FileNotFoundError:
    print("Error: file not found.")
    input("Press ENTER to end.")