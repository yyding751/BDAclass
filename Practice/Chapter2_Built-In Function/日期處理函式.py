import datetime

nowtime=datetime.datetime.now();
#屬性attribute
print("Now:", nowtime)
print("Year",nowtime.year)
print("Month",nowtime.month)
print("Day",nowtime.day)
print("Hour",nowtime.hour)
print("Minute",nowtime.minute)
print("Second",nowtime.second)
#函數function
print("Weekday",nowtime.weekday())
print("Weekday",nowtime.isoweekday())
print("Weekday",nowtime.strftime("%A"))