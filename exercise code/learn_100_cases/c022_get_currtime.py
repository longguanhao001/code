import datetime

curr_datetime = datetime.datetime.now()
print(curr_datetime, type(curr_datetime))

strcurr_datetime = curr_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(strcurr_datetime)

print("year", curr_datetime.year)
print("month", curr_datetime.month)
print("day", curr_datetime.day)
print("hour", curr_datetime.hour)
print("minute", curr_datetime.minute)
print("second", curr_datetime.second)