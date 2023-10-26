#!/usr/bin/env python3

import os

# Function to check if a file exists
def fileExists(filename):
    return os.path.isfile(filename)

if __name__ == "__main__":
    import sys

    # Check if exactly three arguments are provided
    if len(sys.argv) != 4:
        # Display usage error message
        print("Usage: {} input copy copy1".format(sys.argv[0]))
        sys.exit(1)  # Exit with an error code

    # Check if the source file exists
    if not fileExists(sys.argv[1]):
        print("Opening Error!: {} does not exist".format(sys.argv[1]))
        sys.exit(1)

    # Open the source file in read mode
    input_file = open(sys.argv[1], "r")
    if input_file is None:
        print("Error opening source file")
        sys.exit(1)

    # Open the first destination file in write mode
    copy_file = open(sys.argv[2], "w")
    if copy_file is None:
        print("Error opening destination file 1")
        input_file.close()
        sys.exit(1)

    # Open the second destination file in write mode
    copy1_file = open(sys.argv[3], "w")
    if copy1_file is None:
        print("Error opening destination file 2")
        input_file.close()
        copy_file.close()
        sys.exit(1)

    # Copy contents from source to destination files
    ch = input_file.read(1)
    while ch != "":
        copy_file.write(ch)   # Copy to the first destination file
        copy1_file.write(ch)  # Copy to the second destination file
        ch = input_file.read(1)

    # Close all files
    input_file.close()
    copy_file.close()
    copy1_file.close()
    print("Files copied successfully.")
    sys.exit(0)