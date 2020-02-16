# Variable declaration & initialization
f=0
print(f)


# Python is dynamically typed
f="abc"
g="xyz"
print(f)


# Python is strongly typed
#print("abc " + 123) 
# TypeError: can only concatenate str (not "int") to str
print("abc " + str(123))


def someFunction():
    global f
    f="ABC"
    g="XYZ"
    print("Inside someFunction f: " + f)
    print("Inside someFunction g: " + g)


# Variable scope
someFunction()
print("Global f: " + f)
print("Global g: " + g)


del f
#print("Deleted f: " + f)
# Error: name 'f' is not defined


# Output of this script:
# 0
# abc
# abc 123
# Inside someFunction f: ABC
# Inside someFunction g: XYZ
# Global f: ABC
# Global g: xyz
