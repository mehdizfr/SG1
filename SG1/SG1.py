from PIL import Image

import math
import os
import sys  

def GetTextFileName():
    while True:
        filename = input("Enter a .txt filename: ").strip()

        if filename == "":
            print("Error: filename cannot be empty.")
        elif not filename.lower().endswith(".txt"):
            print("Error: filename must end with .txt.")
        else:
            return filename
        
        
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

    img.putdata(pixels)
#Determines where to save the image#
    output_path = os.path.join(os.getcwd(), "IMAGE1.PNG")


    img.save(output_path)

    print(f"Image saved to {output_path}")

    img.show()

print("SG1 Program")
print("This program reads a binary text file and works with images.")


filename = GetTextFileName()

try:
    file = open(filename, "r")
    data = file.read()
    file.close()

    lines = data.splitlines()

    for line in lines:
        if any(char not in "01" for char in line):
            print("Error: file must contain only 0s and 1s.")
            input("Press ENTER to end.")
            raise SystemExit

    if len(lines) < 10:
        print("Error: file must have at least 10 lines.")
        input("Press ENTER to end.")
        raise SystemExit

    length = len(lines[0])

    if length < 20:
        print("Error: each line must have at least 20 characters.")
        input("Press ENTER to end.")
        raise SystemExit

    for line in lines:
        if len(line) != length:
            print("Error: all lines must have the same length.")
            input("Press ENTER to end.")
            raise SystemExit

    print(data)
    
    
    
    
    CreateImage(lines)

except FileNotFoundError:
    print("Error: file not found.")
    input("Press ENTER to end.")
    
       