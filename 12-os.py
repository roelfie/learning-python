import os
from os import path
import datetime
import time

FILENAME = "test.txt"

def main():
    print("OS", os.name)

    print(FILENAME, "exists:", str(path.exists(FILENAME)))
    print(FILENAME, "is a file:", str(path.isfile(FILENAME)))
    print(FILENAME, "is a directory:", str(path.isdir(FILENAME)))

    print("Full path:", str(path.realpath(FILENAME)))
    print("Path and filename:", str(path.split(path.realpath(FILENAME))))

    print("Last modified (long):", time.ctime(path.getmtime(FILENAME)))
    print("Last modified (short):", datetime.datetime.fromtimestamp(path.getmtime(FILENAME)))


if __name__ == "__main__":
    main()
