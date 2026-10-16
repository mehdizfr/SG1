
"""
Programming Language:
    Python 3

Development Environment:
    Thonny IDE

Course:
    CMP SCI 4500 - Software Development
    Fall 2026

Group:
    Group 5

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
    October 13, 2026 - Improved binary file validation and error handling.
    October 14,2026 - Added the image1.png logic to main
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

    NOTE:
    The current version implements filename input, binary text-file
    validation, and displaying the contents of the file.

    The image-processing and pattern-detection portions will be
    integrated with the team's contributions.

Central Data Structures:
    The program uses a list of strings named lines to store the rows
    read from the binary text file.

    The completed program will also use a two-dimensional list named
    ZerosAndOnes to represent pixels from IMAGE2.PNG. Black pixels
    are represented by 0 and other pixel values are represented by 1.

External Files:
    User-selected .txt file:
        Contains rows of binary digits used to create IMAGE1.PNG.

    IMAGE1.PNG:
        Will be generated from the binary text file.

    IMAGE2.PNG:
        A 250 by 250 black-and-white input image used for pattern
        detection.

    IMAGE3.PNG:
        Will be generated from IMAGE2.PNG after detected pattern
        backgrounds are changed to red.

External Resources:
    ChatGPT:
        Used for assistance with the GetTextFileName function,
        binary file validation, and error handling.

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

        # Windows reserves certain names, even when they have
        # file extensions.
        reserved_base = base_name.split(".")[0].upper()

        if reserved_base in reserved_names:
            print(
                "Error: " + base_name
                + " is a reserved Windows filename."
            )
            continue

        if base_name.endswith("."):
            print("Error: filename cannot end with a period.")
            continue

        if len(filename) > 255:
            print("Error: filename is too long.")
            continue

        return filename


def ReadBinaryTextFile(filename):
    """
    Purpose:
        Opens and validates a text file containing binary digits.

    Global Variables:
        None.

    Parameters:
        filename - The name of the text file to open.

    Returns:
        A list of strings containing the valid binary rows.

        The program terminates if the file is missing or invalid.
    """

    try:
        with open(filename, "r") as file:
            data = file.read()

    except FileNotFoundError:
        print("Error: file not found.")
        input("Press ENTER to end.")
        raise SystemExit

    except (PermissionError, UnicodeError, OSError):
        print("Error: unable to read the file.")
        input("Press ENTER to end.")
        raise SystemExit

    lines = data.splitlines()

    # Check for invalid characters.
    for line in lines:
        if any(char not in "01" for char in line):
            print("Error: file must contain only 0s and 1s.")
            input("Press ENTER to end.")
            raise SystemExit

    # The text file must contain at least 10 lines.
    if len(lines) < 10:
        print("Error: file must have at least 10 lines.")
        input("Press ENTER to end.")
        raise SystemExit

    # Every line must contain at least 20 characters.
    for line in lines:
        if len(line) < 20:
            print("Error: each line must have at least 20 characters.")
            input("Press ENTER to end.")
            raise SystemExit

    # All lines must have the same number of characters.
    length = len(lines[0])

    for line in lines:
        if len(line) != length:
            print("Error: all lines must have the same length.")
            input("Press ENTER to end.")
            raise SystemExit

    # Display the valid file contents.
    for line in lines:
        print(line)

    return lines


from PIL import Image

def ConvertImage2():
    """
    Converts IMAGE2.PNG into a list of zeros and ones.
    """
    image = Image.open("IMAGE2.PNG").convert("RGB")
    image.show()
    width, height = image.size

    if width != 250 or height != 250:
        print("Error: IMAGE2.PNG must be 250 by 250.")
        return None

    ZerosAndOnes = []

    for y in range(height):
        row = []

        for x in range(width):
            pixel = image.getpixel((x, y))

            if pixel == (0, 0, 0):
                row.append(0)
            else:
                row.append(1)

        ZerosAndOnes.append(row)

    return ZerosAndOnes


def FindPlusSigns(ZerosAndOnes):
    """
    Finds the 11 by 11 plus-sign pattern.
    Returns the center coordinates of each match.
    """
    centers = []
    height = len(ZerosAndOnes)
    width = len(ZerosAndOnes[0])

    for y in range(height - 10):
        for x in range(width - 10):
            found = True

            for row in range(11):
                for col in range(11):
                    if row == 5 or col == 5:
                        expected = 0
                    else:
                        expected = 1

                    if ZerosAndOnes[y + row][x + col] != expected:
                        found = False
                        break

                if not found:
                    break

            if found:
                centers.append((x + 5, y + 5))

    return centers

def CreateImage3(image2_path, centers):
    """
    Purpose:
        Creates IMAGE3.PNG from IMAGE2.PNG by highlighting the white 
        background pixels of detected 11x11 plus-sign patterns in red.
    
    Parameters:
        image2_path - Path to IMAGE2.PNG
        centers - List of (x, y) center coordinates of detected plus signs
    
    Returns:
        None
    """
    img = Image.open(image2_path).convert("RGB")
    pixels = img.load()
    width, height = img.size

    for (cx, cy) in centers:
        # The 11x11 plus-sign pattern extends 5 pixels out from the center in each direction
        for y in range(cy - 5, cy + 6):
            for x in range(cx - 5, cx + 6):
                if 0 <= x < width and 0 <= y < height:
                    current_pixel = pixels[x, y]
                    # If it's a white background pixel, change it to red (255, 0, 0)
                    if current_pixel == (255, 255, 255) or current_pixel == 255:
                        pixels[x, y] = (255, 0, 0)

    output_path = os.path.join(os.getcwd(), "IMAGE3.PNG")
    img.save(output_path)
    print(f"IMAGE3 saved to {output_path}")
    img.show()

from PIL import Image

import math
import os
import sys 
#Resources
#https://stackoverflow.com/questions/8554282/creating-a-png-file-in-python        
#https://stackoverflow.com/questions/45029829/how-to-properly-set-the-path-to-input-output-file
def CreateImage(lines):
#Image Dismensions
    height = len(lines)
    width = len(lines[0])

    img = Image.new('L', (width, height))
#Empty list of pixels"
    pixels = []
#Read every character in line ,from top to and bottom also left and right
    for line in lines:
        for char in line:
            if char == '0':
                pixels.append(0)
            else:
                pixels.append(255)
#Add pixels
    img.putdata(pixels)
#Determines where to save the image#
    output_path = os.path.join(os.getcwd(), "IMAGE1.PNG")


    img.save(output_path)

    print(f"Image saved to {output_path}")

    img.show()




def main():
    """
    Purpose:
        Runs the SG1 program.

    Global Variables:
        None.

    Parameters:
        None.

    Returns:
        None.
    """

    print("SG1 Program")
    print("This program reads a binary text file and works with images.")

    # Ask the user for the text filename.
    filename = GetTextFileName()

    # Open, validate, and display the binary text file.
    lines = ReadBinaryTextFile(filename)

    print("Binary text file validated successfully.")

    # ------------------------------------------------------------
    # TEAM INTEGRATION SECTION
    # ------------------------------------------------------------
    # Add the team's IMAGE1.PNG code here.
    #
    #Adds the Image1
    CreateImage(lines)
    # Add the team's IMAGE2.PNG and ZerosAndOnes code here.
    ZerosAndOnes = ConvertImage2()

    if ZerosAndOnes is not None:
        centers = FindPlusSigns(ZerosAndOnes)

        print("Number of plus signs:", len(centers))

        for center in centers:
            print("Center coordinates:", center)

        # Create IMAGE3 using the detected plus-sign centers.
        CreateImage3("IMAGE2.PNG", centers)

if __name__ == "__main__":
    main()
