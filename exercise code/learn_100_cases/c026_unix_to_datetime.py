# unix时间戳转换为日期时间格式
import datetime
unix_time =1607476474

datetime_obj = datetime.datetime.fromtimestamp(unix_time)
datetime_str = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
print(datetime_str)