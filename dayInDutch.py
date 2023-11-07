# Write a method that when passed a date as "dd mm yyyy" and returns the date's weekday name in the Dutch culture.
# Examples

# weekday_dutch("21 9 1970") ➞ "maandag"

# weekday_dutch("2 9 1945") ➞ "zondag"

# weekday_dutch("9 11 2001") ➞ "dinsdag"

from datetime import datetime
def weekday_dutch(date):
    dWeek = {
        "Monday":"maandag", "Tuesday":"dinsdag", "Wednesday":"woensdag",
        "Thursday":"donderdag", "Friday":"vrijdag", "Saturday":"zaterdag","Sunday":"zondag"
    }
    
    d = list(map(int, date.split()))[::-1]
    return dWeek[datetime(d[0],d[1],d[2]).strftime("%A")]

print(weekday_dutch("21 9 1970")) # ➞ "maandag"
print(weekday_dutch("2 9 1945")) # ➞ "zondag"
print(weekday_dutch("9 11 2001")) # ➞ "dinsdag"

# from datetime import datetime

# def weekday_dutch(date):
#     d, m, y = map(int, date.split())
#     days = ['zondag', 'maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag']
#     return days[int(datetime(y, m, d).strftime('%w'))]

# import datetime

# NAME = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

# def weekday_dutch(date):
# 	return NAME[datetime.datetime.strptime(date, "%d %m %Y").weekday()]

# from time import strptime
# dutch_days = ['maandag', 'dinsdag', 'woensdag', 'donderdag',
#               'vrijdag', 'zaterdag', 'zondag']
# def weekday_dutch(date):
#     return dutch_days[strptime(date, '%d %m %Y').tm_wday]