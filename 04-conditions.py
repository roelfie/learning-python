# --------------------
# if / elif / else
def compare(x, y):
    if (x > y):
        return 1
    elif (x == y):
        return 0
    else:
        return -1

print(compare(1, 2))
# -1


# --------------------
# Conditional (ternary) operator
# expr1 if (CONDITION) else expr2
def greaterThan(x, y):
    return "Yes" if (x>y) else "No"

print(greaterThan(1, 2))
# No
