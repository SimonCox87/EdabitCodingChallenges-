"""Create a function which returns how many Friday 13ths there are in a given year.
Examples

how_unlucky(2020) ➞ 2

how_unlucky(2026) ➞ 3

how_unlucky(2016) ➞ 1

Notes

Check Resources for some helpful tutorials on the Python datetime module."""

from datetime import datetime
def how_unlucky(y):
    return[datetime(y,i,13).strftime("%a") for i in range(1,13)].count("Fri")

    return sum(datetime(y,i,13).strftime("%a") == "Fri" for i in range(1,13))

print(how_unlucky(2020)) # ➞ 2
print(how_unlucky(2026)) # ➞ 3
print(how_unlucky(2016)) # ➞ 1

"""from datetime import date

def how_unlucky(y):
	return sum(date(y, m, 13).strftime('%A') == 'Friday' for m in range(1, 13))"""

"""import calendar

def how_unlucky(y):
    return sum(calendar.weekday(y, m, 13) == 4 for m in range(1, 13))"""

"""from datetime import datetime as dt
def how_unlucky(y):
	return sum(dt.strftime(dt(y,m,13),"%a")=="Fri" for m in range(1,13))"""