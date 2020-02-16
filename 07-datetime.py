from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    print("Today is", today)
    print("Date components:", today.day, today.month, today.year)
    print("Today's weekday #:", today.weekday())
    print("--------------------")
    print("Now is", datetime.now())
    print("The time is", datetime.time(datetime.now()))

# --------------------
if __name__ == "__main__":
    main()

