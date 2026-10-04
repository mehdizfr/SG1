def GetTextFileName():
    while True:
        filename = input("Enter a .txt filename: ").strip()

        if filename == "":
            print("Error: filename cannot be empty.")
        elif not filename.lower().endswith(".txt"):
            print("Error: filename must end with .txt.")
        else:
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