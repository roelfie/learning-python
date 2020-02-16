# ----------
# Void function
def func1():
    print("Inside func1")

func1()
# Inside func1
print(func1)
# <function func1 at 0x10eded310>
print(func1())
# Inside func1
# None


# ----------
# Function arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

print(func2(10, 20))
# 10 20
# None


# ----------
# Function with return value
def cube(x):
    return x*x*x

print(cube(3))
# 27


# ----------
# Function with default argument value
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

print(power(2))
# 2
print(power(2, 3))
# 8


# ----------
# Function parameters random order
print(power(x=3, num=2))
# 8


# ----------
# Function with varargs
def add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(add(1,2,3,4,5,6,7,8,9,10))

