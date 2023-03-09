#1
from datetime import date, timedelta
day = date.today() - timedelta(5)
print("Current Date: ",end="")
print(date.today())
print("5 days ago: ",end="")
print(day)


#2
yesterday = date.today() - timedelta(1)
tomorrow = date.today() + timedelta(1)
print('Current Date :', date.today())
print('Yesterday was :', yesterday)
print('Tomorrow will be:', tomorrow)


#3
import datetime
day = datetime.datetime.today().replace(microsecond = 0)
print()
print(day)
print()


#4
from datetime import datetime, time


def date_diff(d2, d1):
    timedelta = d2 - d1
    return timedelta.days * 24 * 3600 + timedelta.seconds


# Specified date
date1 = datetime.strptime('2023-03-09 16:12:00', '%Y-%m-%d %H:%M:%S')
# Current date
date2 = datetime.now()
print("\n%d seconds" % (date_diff(date2, date1)))
print()