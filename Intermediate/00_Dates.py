# Dates

# Getting datetime Information
from datetime import datetime
now = datetime.now()
print(now)                      # 2024-10-15 17:21:39.103257
day = now.day                   # 15
month = now.month               # 10
year = now.year                 # 2024
hour = now.hour                 # 17
minute = now.minute             # 25
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('Timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}') # 15/10/2024, 17:27
# Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.


'''Formatting Date Output Using strftime'''
from datetime import datetime
new_year = datetime(2025,1,1)
print(new_year)      # 2025-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) # 1 1 2025 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}') # 1/1/2025, 0:0


'''String to Time using strptime'''
from datetime import datetime
date_string = "15 October, 2024"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

'''Using date from datetime'''
from datetime import date
d = date(2025, 1, 1)
print(d)
print('Current date:', d.today())   # 2024-10-15
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2024
print("Current month:", today.month) # 10
print("Current day:", today.day)     # 15


''' Time Objects to Represent Time '''
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)


''' Difference Between Two Points in Time Using '''
today = date(year=2024, month=10, day=15)
new_year = date(year=2025, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2024, month = 10, day = 15, hour = 5, minute = 53, second = 0)
t2 = datetime(year = 2025, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff)  # Time left for new year: 77 days, 18:07:00


''' Difference Between Two Points in Time Using timedelta '''
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)