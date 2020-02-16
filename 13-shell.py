import os
from os import path
import shutil
from zipfile import ZipFile


FILENAME = "test.txt"


def main():

    if path.exists(FILENAME):
        src = path.realpath(FILENAME)
        dst = src + ".bck"

        # create a file copy (contents only)
        shutil.copy(src,dst)

        # create a file copy (including metadata)
        shutil.copystat(src,dst)

        # rename a file
        os.rename(FILENAME, "test-renamed.txt")
        os.rename("test-renamed.txt", FILENAME)

        # archive current directory in a zip file
        # root_dir, tail = path.split(src)
        # shutil.make_archive("archive-all", "zip", root_dir)

        # Create a new zip file, and add specific files to it
        with ZipFile("archive-txt.zip", "w") as zf:
            zf.write("test.txt")

        # Create a new zip file, and add all *.py files to it
        with ZipFile("archive-py.zip", "w") as zf: 
            dir = os.getcwd()
            for folderName, subfolders, filenames in os.walk(dir):
                for filename in filenames:
                    name, ext = os.path.splitext(filename)
                    if (ext == '.py'):
                        filePath = os.path.join(folderName, filename)
                        zf.write(filePath)


if __name__ == "__main__":
    main()
