"""
Python DateTime, TimeDelta, Strftime(Format) with examples
In Python, date, time and datetime classes provides a number of function to deal
with dates, times and time intervals. Date and datetime are an object in Python,
so when you manipulate them, you are actually manipulating objects and not
string or timestamps.

The datetime classes in Python are categorized into main 5 classes.

.date - Manipulate just date (Month, day, year)
.time - Time independent of the day (Hour, minute, second, microsecond)
.datetime - Combination of time and date
.timedelta - A duration of time used for manipulating dates
.tzinfo - An abstract class for dealing with time zones

https://www.programiz.com/python-programming/datetime
"""
import datetime
from datetime import date

#What's inside datetime?
print(dir(datetime))

#EX1: Get current date and time
datetime_object = datetime.datetime.now()
print(datetime_object)

#EX2: Get current date
date_object = datetime.date.today()

#Ex3: Date object to represent a dates
d=datetime.date(2019,4,13)
#date() is a constructor takes three arguments: year, month and day.
print(d)

#EX4: Get date from a timestamp
#A Unix timestamp is the number of seconds btw a particular date and
#1970/01/01 at UTC.
timestamp=date.fromtimestamp(1326244364)
print("Date =", timestamp)

#EX5: print today's year, month and day
today=date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

#Ex6: Time object to represent time
from datetime import time
#time(hour=0, minute=0, second=0)
a=time()
print("a=", a)
b=time(11, 34, 56)
print("b=", b)
c=time(hour=11,minute=34, second = 56)
print("c=", c)
d=time(11, 34, 56, 234566)
print("d=", d)

#Ex7: print hour, minute, second and microsecond

a=time(11, 34, 56)
print("hour =", a.hour)
print("minute =", a.minute)
print("second = ", a.second)
print("microsecond =", a.microsecond)

#Ex8: Python datetime object
from datetime import datetime
#datetime(year, month, day)
a=datetime(2018,11,28)
print(a)
#datetime(year, month, day, hour, minute, second, microsecond)
b=datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)
# The first three arguments year, month and day in the datetime() constructor are
#mandatory

#EX9: Print year, month, hour, minute and timestamp
from datetime import datetime
a=datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year=", a.year)
print("month=", a.month)
print("hour=", a.hour)
print("minute=", a.minute)
print("timestamp=", a.timestamp())

#timedelta
"""
generally used for calculating differences in dates and also can be used for date
manipulations in Python. It is one of the easiest ways to perform date manipulations.
"""
from datetime import datetime, timedelta
ini_time_for_now=datetime.now()
future_date_after_2days = ini_time_for_now + timedelta(days=2)
before_2hours =  ini_time_for_now - timedelta(hours=2)

#Ex10: Time duration in seconds
t=timedelta(days=5, hours=1, seconds=33, microsecond=233423)
print("total seconds =", t.total_seconds())

#https://www.programiz.com/python-programming/datetime/strftime
#convert date, time and datetime objects to its equivalent string
# strftime() method takes one or more format codes as an argument and returns a formatted string based on it

#EX1:
from datetime import datetime
now=datetime.now()
date_time=now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)


#strptime() method creates a datetime object from a given string.
#EX:
from datetime import datetime
date_string = "21 June, 2018"
print("date_string =", date_string)
print("type of date_string = ", type(date_string))

date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object=", date_object)
print("type of date_object =", type(date_object))

from datetime import datetime
dt_string = "12/11/2018 09:15:32"
# Considering date is in dd/mm/yyyy format
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1 =", dt_object1)
# Considering date is in mm/dd/yyyy format
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2 =", dt_object2)
