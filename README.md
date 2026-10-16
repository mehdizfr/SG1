# SG1 - Manipulating Files and Images Using Python 3

CMP SCI 4500   
Fall 2026  
Group 5  
Python 3  
Thonny IDE

## Group Members

- Mehdi Zafferi
- Rahul Anilkumar
- Klara Pere
- Scott Smith
- Armando Montoya

## Program Description

SG1 is a Python program that reads and validates a text file containing binary digits (0s and 1s), converts that data into a black-and-white PNG image, and analyzes a separate image to locate specific 11x11 plus-sign patterns.

The program produces three images:
IMAGE1.PNG: Generated from the binary text file. Zeros become black pixels, and ones become white pixels.
IMAGE2.PNG: [MUST BE PROVIDED.] A 250x250 black-and-white image supplied as input. The program converts its pixels into a two-dimensional matrix of zeros and ones.
IMAGE3.PNG: Generated from IMAGE2.PNG. The white background pixels surrounding detected plus signs are changed to red while the black plus signs remain unchanged.

The program also displays the number of plus signs detected and the center coordinates of each pattern.

## Requirements

Python 3
Tested in Thonny IDE enviroment
Pillow (PIL) library
A valid binary text file [Requirements below]
IMAGE2.PNG (250x250 pixels)

## Installing Pillow

Pillow is required to read, create, and save PNG images.

In Thonny:
1. Open Tools > Manage packages.
2. Search for Pillow.
3. Click Install.

## How to Run the Program

1. Open Thonny IDE.
2. Open the SG1 Python script.
3. Make sure the binary text file and IMAGE2.PNG are located in the program's working directory.
4. Run the program.
5. Enter the binary text filename when prompted, including the .txt extension.
6. The program will validate and display the binary text file.
7. The program will create and display IMAGE1.PNG.
8. The program will load and display IMAGE2.PNG.
9. The program will search for 11x11 plus-sign patterns and display their center coordinates.
10. The program will create, save, and display IMAGE3.PNG.
11. Press ENTER when prompted to end the program.
It is important ALL files are in the same folder.

## Input File Requirements

The binary text file must:

Have a filename ending in .txt.
Contain only zeros and ones.
Contain at least 10 lines.
Have at least 20 characters per line.
Have the same number of characters on every line.

IMAGE2.PNG must:
be exactly 250x250 pixels.

## Expected Output
For a successful test using valid.txt and the group's two-plus-sign test image:
Number of plus signs: 2  
Center coordinates: (55, 65)  
Center coordinates: (185, 175)

The program also creates IMAGE1.PNG and IMAGE3.PNG in the current directory.

## Error Handling

The program checks for invalid filenames, missing or invalid binary text files, and incorrect IMAGE2.PNG dimensions.

If an input file is invalid, the program displays an error message. Invalid text-file inputs cause the program to stop after the user presses ENTER.


