import datetime

def get_date_range(begin_date, end_date):
    date_list=[]
    while begin_date <= end_date:
        date_list.append(begin_date)
        begin_date_obj = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        days1_timedelta = datetime.timedelta(days=1)
        begin_date = (begin_date_obj + days1_timedelta).strftime("%Y-%m-%d")

    return date_list






begin_date="2023-03-19"
end_date = "2023-04-02"

date_list = get_date_range(begin_date, end_date)
print(date_list)