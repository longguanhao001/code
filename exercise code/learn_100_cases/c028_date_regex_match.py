# 输入一个字符串，使用正则表达式判断是否是日期格式
import re
def date_is_right(date):
    # return re.match("\d{4}-\d{2}-\d{2}", date) is not None
    return re.match("\d{4}(-|\/)\d{2}(-|\/)\d{2}", date) is not None # 匹配YYYY-MM-DD和YYYY/MM/DD格式的日期
date1 = "2022-05-20"
date2 = "2022-5-20"
date3 = "2022-05-1"
date4 = "20220520"
date5 = "2022/05/20"


print(date1, date_is_right(date1))
print(date2, date_is_right(date2))
print(date3, date_is_right(date3))
print(date4, date_is_right(date4))
print(date5, date_is_right(date5))