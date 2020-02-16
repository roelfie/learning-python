from datetime import datetime

def main():
    now = datetime.now()

    print(now.strftime("Current year: %Y (short: %y)"))
    print(now.strftime("Current month: %B (short: %b)"))
    # February (short: Feb)
    print(now.strftime("Current day: %d"))

    print(now.strftime("Local date and time: %c"))
    # Sun Feb 16 17:48:26 2020
    print(now.strftime("Local date: %x"))
    # 02/16/20
    print(now.strftime("Local time: %X"))
    # 17:48:26

    print(now.strftime("Current time: %I:%M:%S %p"))
    # 05:48:26 PM
    print(now.strftime("Current time: %H:%M:%S"))
    # 17:48:26


# --------------------
if __name__ == "__main__":
    main()

