import datetime

def get_diff_date(pdate, days):
    pdate_obj = datetime.datetime.strptime(pdate, "%Y-%m-%d")
    time_gap = datetime.timedelta(days=days)

    padte_result = pdate_obj - time_gap
    return padte_result.strftime("%Y-%m-%d")

print(get_diff_date("2023-03-19", 1))
print(get_diff_date("2022-03-19", 3))
print(get_diff_date("2023-03-19", 5))
print(get_diff_date("2023-03-19", 7))
print(get_diff_date("2023-03-19", 10))
print(get_diff_date("2023-04-01", 3))
print(get_diff_date("2023-02-28", 3))