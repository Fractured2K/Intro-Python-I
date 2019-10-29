"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

date = datetime.now()
argsLength = len(sys.argv)


def argsDate(num):
    return int(sys.argv[num])


if argsLength == 1:
    date = date
elif argsLength == 2:
    date = datetime(date.year, argsDate(1), 1)
elif argsLength == 3:
    date = datetime(argsDate(1), argsDate(2), 1)
else:
    print('Enter a year e.g 2019 and month e.g 9 to print out that calendar year and month')
    sys.exit()

print(calendar.month(date.year, date.month))
