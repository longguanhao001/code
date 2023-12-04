import datetime

birthday = "1997-05-01"
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
curr_datetime = datetime.datetime.now()
print(curr_datetime, type(curr_datetime))

minus_datetime = curr_datetime - birthday_date
print(minus_datetime, type(minus_datetime))