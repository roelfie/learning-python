def main():
    x = 0


    # --------------------
    # while
    while (x < 3):
        print(x)
        x = x + 1


    # --------------------
    # for loop (range)
    for x in range(5,10):
        print(x)
        # 5, 6, 7, 8, 9


    # --------------------
    # for loop (break)
    for x in range(5,10):
        if (x==8): break
        print(x)
        # 5, 6, 7


    # --------------------
    # for loop (continue)
    for x in range(5,10):
        if (x%2 == 0): continue # skip even numbers
        print(x)
        # 5, 7, 9


    # --------------------
    # for loop (collection)
    days=["Mon","Tue","Wed","Thu","Fri"]
    for d in days:
        print(d)


    # --------------------
    # enumerate()
    for i,d in enumerate(days):
        print(i, d)
        # 0 Mon
        # 1 Tue
        # 2 Wed
        # ...


# --------------------
# This tells python to execute the main function only if this *.py scripts was executed directly
if __name__ == "__main__":
    main()
