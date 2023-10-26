#Dazarus Chapman
import grp
import os
from pathlib import Path
import pwd
import sys
from stat import S_ISBLK, S_ISCHR, S_ISDIR, \
    S_ISDOOR, S_ISGID, S_ISLNK, S_ISREG, \
    S_ISSOCK, S_ISUID, S_ISVTX, S_IXGRP, S_IXOTH, S_IXUSR


def file_type_letter(mode: int) -> int:
    c = '?'

    if S_ISREG(mode):
        c = '-'
    elif S_ISDIR(mode):
        c = 'd'
    elif S_ISBLK(mode):
        c = 'b'
    elif S_ISCHR(mode):
        c = 'c'
    elif S_ISLNK(mode):
        c = 'l'
    elif S_ISSOCK(mode):
        c = 's'
    elif S_ISDOOR(mode):
        c = 'D'

    return c


def ls_perms(mode: int) -> str:
    rwx = ["---", "--x", "-w-", "-wx",
           "r--", "r-x", "rw-", "rwx"]

    bits = [0] * 10

    bits[0] = file_type_letter(mode)
    bits[1] = rwx[(mode >> 6) & 7]
    bits[4] = rwx[(mode >> 3) & 7]
    bits[7] = rwx[(mode & 7)]

    if mode & S_ISUID:
        bits[3] = 's' if (mode & S_IXUSR) else 'S'
    if mode & S_ISGID:
        bits[6] = 's' if (mode & S_IXGRP) else 'l'
    if mode & S_ISVTX:
        bits[9] = 't' if (mode & S_IXOTH) else'T'

    bits = [i for i in bits if i != 0]
    return ''.join(bits)


def get_filename_ext(filename: str) -> str:
    return Path(filename).suffix


if __name__ == "__main__":
    argc = len(sys.argv) # grab the length of aguments in code line

    if argc < 4:
        print("Usage: python3 dazaruschapman_hw4.py <operation> <ext> <directory> [<search_keyword>]") 
        sys.exit(1) # if number of arguments is under 4 whhen using Search Keyword exit 

    operation = sys.argv[1] # details or search
    extension = sys.argv[2] # file extension
    directory = sys.argv[3] # file path to directory
    search_keyword = sys.argv[4] if len(sys.argv) > 4 else None

    if operation == "details":
        for filename in os.listdir(directory):
            if filename.endswith(extension):
                filepath = os.path.join(directory, filename)
                buf = os.stat(filepath)
                mode = buf.st_mode
                perms = ls_perms(mode)
                pw = pwd.getpwuid(buf.st_uid) # get user ID
                gr = grp.getgrgid(buf.st_gid) # get group ID

                print(f"filenames: {filename}")
                print(f"Permissions: {perms}") # print file permissions
                print(f"name: {pw.pw_name}")   # print file name
                print(f"group: {gr.gr_name}\n") # print group name

    
    elif operation == "search":
        if search_keyword is not None:
            for filename in os.listdir(directory): # checking every file in directory given
                if filename.endswith(extension): # pulling only the files with the .txt extension or whichever one provided
                    filepath = os.path.join(directory, filename) 
                    with open(filepath, 'r') as file:
                        contents = file.read()
                        if search_keyword in contents:
                            print(f'The keyword "{search_keyword}" found in: {filename}') # Print out the word found and the file name it was found at