FILENAME = "test.txt"

def main():

    # "w" = (over)write ; "a" = append ; "+" create if non-existent
    print("Write file", FILENAME)
    f = open(FILENAME, "w+")
    for i in range(10):
        f.write("This is line " + str(i) + "\r\n")
    f.close()


    print("Read file", FILENAME)
    f = open(FILENAME, "r")
    if f.mode == 'r':
        contents = f.read()
        print(contents)
    f.close()


    print("Read file (line by line)", FILENAME)
    f = open(FILENAME, "r")
    if f.mode == 'r':
        lines = f.readlines()
        for line in lines:
            print(line)
    f.close()


if __name__ == "__main__":
    main()
