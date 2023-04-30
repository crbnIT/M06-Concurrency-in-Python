'''
Corbyn Eaker
M06_Concurrency_in_Python.py
This program completes and documents the different problems to solve in chapter 13 for assignemnt Concurrency in Python (13.1, 13.2, 13.3)
'''

# import all from datetime (could have just used "from datetime import date, datetime" but I was playing with other functionality)
from datetime import *

# create variables to store today's date and a format
now = date.today()
fmt = '%d%b%Y'

# 13.1
# open today.txt and write now variable formatted
with open('today.txt', 'w') as file:
    file.write(now.strftime(fmt))

# 13.2
# open file and read contents, convert contents to datetime, format and store in variable today_string
with open('today.txt', 'r') as file:
    today_string = datetime.strptime(file.read(), fmt)

# 13.3
# create variables for the year month and day, set them to today_string's respective methods
year = today_string.year
month = today_string.month
day = today_string.day

# print parsed today_string
print(f'Year: {year}\nMonth: {month}\nDay: {day}')

