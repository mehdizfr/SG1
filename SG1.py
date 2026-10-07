def GetTextFileName():
    """
    Gets a valid Windows 11 text filename from the user.

    Global variables used:
        None.

    Parameters:
        None.

    Returns:
        A valid filename ending in .txt.

    NOTE:
        This function was developed with assistance from ChatGPT.
    """

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

except FileNotFoundError:
    print("Error: file not found.")
    input("Press ENTER to end.")